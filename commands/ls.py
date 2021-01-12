from custom_types import UserbotCommand, Argument
from time import time, strftime, localtime
from asyncio import sleep


class Command(UserbotCommand):
    def __init__(self, client):
        super().__init__(
            client,
            command="ls",
            mutually_exclusive_arguments=[
                [
                    Argument(
                        "--from",
                        options={
                            "help": "list the messages from the user id",
                            "type": int,
                        },
                    ),
                    Argument(
                        "--mine",
                        options={
                            "action": "store_true",
                            "help": "list the messages from yourself",
                        },
                    ),
                    Argument(
                        "--from-reply",
                        options={
                            "action": "store_true",
                            "help": "list messages from the sender of the reply message",
                        },
                    ),
                ],
            ],
            sub_commands_required=False,
            arguments=[
                Argument(
                    "--limit",
                    options={"type": int, "help": "limit for the number of messages",},
                ),
            ],
            description="utility to list messages from specific user in a chat.",
        )

    async def handler(self, event, args):
        message_count = 0
        EDIT_EVERY_NTH_MESSAGE = 10

        user = None
        user_display_name = ""

        initial_time = time()

        if args.mine:
            user = "me"
            user_display_name = "your"
        elif args.from_reply:
            replied_message = await self.client.get_messages(
                event.to_id, ids=event.message.reply_to_msg_id
            )
            user = replied_message.from_id
            user_display_name = f"user: {replied_message.from_id}"

        msg_content = f"List of {user_display_name} messages in this chat [ { 'last ' + str(args.limit) if args.limit else 'all' } messages ] :\n==============\n"

        msg = await event.message.reply(msg_content)
        async for message in self.client.iter_messages(
            event.message.to_id,
            from_user=user,
            limit=args.limit + 2 if args.limit else None,
        ):
            if message.id in [msg.id, event.message.id]:
                continue
            message_count += 1
            msg_content += f'\n{message.id}    "`{message.text[:22]} ...`"'
            if message_count % EDIT_EVERY_NTH_MESSAGE == 0:
                msg = await msg.edit(
                    msg_content
                    + f"\n\n------------\n`Fetched {message_count} messages in {strftime('%M:%S', localtime(time() - initial_time))}`"
                )
                await sleep(2)

        if message_count == 0:
            msg_content += f"\n\n`No messages have been found`."

        msg = await msg.edit(
            msg_content
            + f"\n\n------------\n`[✓] Fetched a total of {message_count} messages in {strftime('%M:%S', localtime(time() - initial_time))}`"
        )

