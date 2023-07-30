import telethon.errors.rpcerrorlist
import config
from telethon import functions


async def check_username(username, session):
    async with telethon.TelegramClient(f'{session}', config.API_ID, config.API_HASH, device_model="iPhone 13 Pro Max",
                                       system_version="14.8.1", app_version="8.4", lang_code="en",
                                       system_lang_code="en-US") as client:
        try:
            await client.get_entity(username)
            print('-' * 100)
            print(f'{username} - Занят')
            print('-' * 100)
            return False
        except ValueError:
            try:
                await client(functions.account.CheckUsernameRequest(username=username))
                print('-' * 100)
                print(f'{username} - Свободен')
                print('-' * 100)
                return True
            except telethon.errors.UsernameInvalidError:
                print('-' * 100)
                print(f'{username} - На продаже / Некорректный')
                print('-' * 100)
                return False
            except telethon.errors.FloodWaitError as e:
                print('-' * 100)
                print(f'{session} - Отлетела')
                print('-' * 100)
                return e.seconds
            except telethon.errors.UsernamePurchaseAvailableError:
                print('-' * 100)
                print(f'{username} - На продаже / Некорректный')
                print('-' * 100)
                return False
            except Exception as e:
                print('-' * 100)
                print(f'Ошибка {session}, при обработке {username}: {e}')
                print('-' * 100)
                print(type(e).__name__)
                return False
        except telethon.errors.UsernameInvalidError:
            print('-' * 100)
            print(f'{username} - На продаже / Некорректный')
            print('-' * 100)
            return False
        except telethon.errors.FloodWaitError as e:
            print('-' * 100)
            print(f'{session} - Отлетела')
            print('-' * 100)
            return e.seconds
        except Exception as e:
            print('-' * 100)
            print(f'Ошибка {session}, при обработке {username}: {e}')
            print('-' * 100)
