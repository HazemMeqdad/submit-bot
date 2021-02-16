import discord
from discord.ext import commands
import asyncio
import json


with open('./config.json', 'r') as f:
    config = json.load(f)


class Submit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="submit", aliases=config['aliases']['submit'])
    @commands.guild_only()
    @commands.cooldown(1, int(config["cooldown"]), commands.BucketType.user)
    async def submit_command(self, ctx):
        channel = self.client.get_channel(int(config['submit_channel']))  # id channel
        answers = []
        embed = discord.Embed(
            description=ctx.author.id,
            color=ctx.author.color,
            timestamp=ctx.message.created_at
        )
        m = "You have 3 minutes to answer each question"
        if config['language'] == "ar":
            m = "لديك 3 دقائق للإجابة على كل سؤال"
        await ctx.author.send(
            embed=discord.Embed(
                description=m,
                color=0xf7072b))
        await ctx.message.add_reaction('✅')

        def check(m):
            return m.author == ctx.author and m.author == ctx.author and str(m.channel.type) == "private"
        nam = 0
        for i in config['questions']:
            nam += 1
            await ctx.author.send(embed=discord.Embed(
                    description=i,
                    color=0xf7072b).set_author(name=f"{nam}/{len(config['questions'])}"))
            try:
                msg = await self.client.wait_for('message', timeout=180.0, check=check)
            except asyncio.TimeoutError:
                m = 'You have exceeded the time specified for submit'
                if config['language'] == "ar":
                    m = "لقد تجاوزت الوقت المحدد للإرسال"
                await ctx.author.send(embed=discord.Embed(
                    description=m,
                    color=0xf7072b))
                return
            else:
                answers.append(msg.content)

        for kay, value in enumerate(config["questions"]):
            embed.add_field(
                name=f"{kay} - {value}:",
                value=answers[kay],
                inline=False
            )
        embed.set_author(name=self.client.user.display_name, icon_url=self.client.user.avatar_url)
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        m = "rect ✅ to send your submit\nrect ❎ to cancel yot submit"
        if config['language'] == "ar":
            m = "اضغط ✅ لارسال تقديمك\nاضغط ❌ للغاء تقديمك"
        message = await ctx.author.send(embed=discord.Embed(
            description=m,
            color=discord.Color.green()
        ))
        await message.add_reaction("✅")
        await message.add_reaction("❎")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]

        try:
            reaction, user = await self.client.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "✅":
                await channel.send(embed=embed)
                m = "✅ Your submit has been sent successfully"
                if config['language'] == "ar":
                    m = "✅ تم ارسال تقديمك في نجاح"
                await message.edit(embed=discord.Embed(
                    description=m,
                    color=discord.Color.green()
                ))
            elif str(reaction.emoji) == "❎":
                m = "❌ Your submit has been cancel"
                if config['language'] == "ar":
                    m = "❌ تم الغاء تقديمك"
                await message.edit(embed=discord.Embed(
                    description=m,
                    color=discord.Color.red()
                ))
                pass
            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()

    @submit_command.error
    async def submit_error(self, ctx, error):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(
                description="❌ Please open your DM before applying and reapply again after 24h",
                color=0xf7072b
            ))
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            await ctx.send(embed=discord.Embed(
                description="❌ It seems that you have chosen the wrong answer. You can reapply again after {}".format(
                    "%d hour, %02d minutes, %02d seconds" % (h, m, s)),
                color=0xf7072b
            ))
        else:
            pass

    @commands.command(name="accept", aliases=config['aliases']['accept'])
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def accept_command(self, ctx, member: discord.Member):
        m = "✅ Done been accepted successfully"
        if config['language'] == "ar":
            m = "✅ تم القبول بنجاح"
        await ctx.send(embed=discord.Embed(
            description=m,
            color=0x03ff74
        ))
        await member.add_roles(discord.utils.get(member.guild.roles, name=config['role']))
        m = "✅ You have been accepted successfully"
        if config['language'] == "ar":
            m = "✅ تم قبولك بنجاح"
        await member.send(embed=discord.Embed(
            description=m,
            color=0x03ff74
        ))

    @commands.has_permissions(administrator=True)
    @accept_command.error
    async def accept_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                description="{}accept <member or DI>".format(self.client.command_prefix),
                color=0xf7072b
            ))
        if isinstance(error, commands.MissingPermissions):
            pass

    @commands.command(name='reject', aliases=config['aliases']['reject'])
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def reject_command(self, ctx, member: discord.Member, *, reason):
        m = f"✅ Done been Unfortunately for {member.mention}"
        if config['language'] == "ar":
            m = f"✅ تم رفض {member.mention}"
        await ctx.send(embed=discord.Embed(
            description=m,
            color=0x03ff74
        ))
        m = f"❌ You have Unfortunately, you were rejected because of:\n{reason}\nIf you have any objections, please contact {ctx.author}"
        if config['language'] == "ar":
            m = f"❌ للاسف لقد تم رفضك للأسف بسبب:\n{reason}\nإذا كان لديك أي اعتراضات ، يرجى التواصل مع {ctx.author}"
        await member.send(embed=discord.Embed(
            description=m,
            color=0xf7072b
        ))

    @commands.has_permissions(administrator=True)
    @reject_command.error
    async def reject_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                description="{}reject <member or DI>".format(self.client.command_prefix),
                color=0xf7072b
            ))
        if isinstance(error, commands.MissingPermissions):
            pass


def setup(client):
    client.add_cog(Submit(client))
# Copyright (c) 2021 NamNam#0090 & OTTWAW team
