from .exclusiveroles import ExclusiveRoles

__red_end_user_data_statement__ = "This cog does not store end user data."


def setup(bot):
    bot.add_cog(ExclusiveRoles(bot))
