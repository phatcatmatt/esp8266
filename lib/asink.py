import asyncio

# state = False


# async def main():
#     if state == True:
#         print('things are true')
#     await asyncio.sleep(5)
#     print('last')
#     # else:
#     #     print('things are false')

# asyncio.run(main())

async def timer():
    print('timer go');
    try:
        await asyncio.sleep(5)
        print('slept for 5')
    except asyncio.CancelledError:
        print('timer cancelled')
        raise
    finally:
        print('finally')

async def main():
    task = asyncio.create_task(timer())
    await task
    print('task done')

asyncio.run(main())