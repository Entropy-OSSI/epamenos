class DSnowflake:
    DISCORD_EPOCH = 1420070400000

    def __init__(self, snowflake: int) -> None:
        self.snowflake: int = snowflake

    @property
    def timestamp(self) -> int:
        return ((self.snowflake >> 22) + self.DISCORD_EPOCH) // 1000

class DEmbed:
    pass

class DAllowedMentions:
    pass

class DMessageReference:
    pass

class DComponent:
    pass

class DAttachment:
    pass
