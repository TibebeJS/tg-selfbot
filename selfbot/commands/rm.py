from selfbot.types import UserbotCommand, Argument
from time import time, strftime, localtime
from asyncio import sleep


class Command(UserbotCommand):
    def __init__(self, instance):
        super().__init__(
            instance,
            command="rm",
            sub_commands_required=False,
            arguments=[
                Argument(
                    "--limit",
                    options={"type": int, "help": "limit for the number of messages",},
                ),
                Argument(
                        "--quiet",
                        options={
                            "action": "store_true",
                            "help": "quiet mode (no messages)",
                        },
                    ),
            ],
            description="utility to list messages from specific user in a chat.",
        )

    async def handler(self, event, args):
        current_value = 0
        max_num_of_dots = 6
        active = '▨'
        passive = '□'
        progress = ''
        total_messages = 0

        message_count = 0
        EDIT_EVERY_NTH_MESSAGE = 10

        if args.quiet:
            await event.message.delete()
        else:
            msg = await event.message.reply(f"stating purging process ...")

        # TODO: check if the user is admin (if --mine is not specified)

        async for message in self.client.iter_messages(event.message.to_id, from_user='me'):
            if not args.quiet and message.id in [ msg.id, event.message.id ]: continue

            await message.delete()

            total_messages += 1
            message_count += 1

            if not args.quiet and (message_count % EDIT_EVERY_NTH_MESSAGE == 0 or message_count == 1):
                current_value += 1
                current_value %= max_num_of_dots
                progress = passive * (current_value) + active + passive * (max_num_of_dots - current_value - 1)
                msg = await msg.edit(f'[{progress}] purging in progress... [{total_messages} msgs. purged]')

        if not args.quiet:
            await msg.edit(f'[✓] messages have been purged!')
