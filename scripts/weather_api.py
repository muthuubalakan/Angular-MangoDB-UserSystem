import asyncio
import aiohttp


async def fetch(client, api_url):
    async with client.get(api_url) as resp:
        assert resp.status == 200
        return await resp.json()

async def main():
    url = "https://reqres.in/api/users?page=2"
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, url)
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
