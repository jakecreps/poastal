import requests

def hulu_email(email):

    cookies = {
        '_suf_id': '4ed13ad1-0406-47a3-8e2f-3418eafa9325',
        'ak_bmsc': '77D1E243A39B647D2E540D5B9174079F~000000000000000000000000000000~YAAQLHhAF+M+V92GAQAAwzsSAhPje39WIQKvA+pUtyVi/7MnD+u6EdpWU28kd+a4Wq8dbctFRnmrCbVxfX2qApcRZ//QCbJbhdZkeDs1MLRE2eSK7jISG8zMpXewraSpHafHs7cp8CK3i3WJFXj+JpLiQuhyXZFiondKPeGx1QHdK+8bTGIIkt2SUP6XptH+P4SmAwgtLpfGGtf70F1marcvrpy1WOtjF1n7caMN3VGNw0kld+KOEbLrbKbgtQkAmO4D3gFT2+i0aWXpbWf8tWG7ZNBRkmEy18CDOMedOEN2cQZeW6ZeV9MCmWd9IRDWOgdlAcGU1Q5FDwj8VuiIWWNrKzKR4BiTZs0zHlIXUB1EerJOIVsk7OaBQU5dE/TbixGGPzlu3TCODFFx',
        'bm_sv': '3F3AB4C8DC370B5D32956C52A635061B~YAAQLHhAF0c/V92GAQAAIlkSAhOTbV5HroQ3S9PgshkVv/JLZIzeXWZzp0trYgw7Z8f6qmG8fohIFaT1BGx5MWVXzBex4rSLNt4vWRQj70ArEnh2mauiDlafc6eST2k6JgxnnPcBp4ceAtu+l/7iLrnAqY0AhRIC1Ux3AZJjeX7JoLVN/PQ6Oags9NIowJtbXNo/D1TCdPx6pLGQ9ucHagfKI3AL1Bb4dWw4J+jqM0+NK7UEgq//f5bOgqPgRSw=~1',
    }

    headers = {
        # 'Cookie': '_suf_id=4ed13ad1-0406-47a3-8e2f-3418eafa9325; ak_bmsc=77D1E243A39B647D2E540D5B9174079F~000000000000000000000000000000~YAAQLHhAF+M+V92GAQAAwzsSAhPje39WIQKvA+pUtyVi/7MnD+u6EdpWU28kd+a4Wq8dbctFRnmrCbVxfX2qApcRZ//QCbJbhdZkeDs1MLRE2eSK7jISG8zMpXewraSpHafHs7cp8CK3i3WJFXj+JpLiQuhyXZFiondKPeGx1QHdK+8bTGIIkt2SUP6XptH+P4SmAwgtLpfGGtf70F1marcvrpy1WOtjF1n7caMN3VGNw0kld+KOEbLrbKbgtQkAmO4D3gFT2+i0aWXpbWf8tWG7ZNBRkmEy18CDOMedOEN2cQZeW6ZeV9MCmWd9IRDWOgdlAcGU1Q5FDwj8VuiIWWNrKzKR4BiTZs0zHlIXUB1EerJOIVsk7OaBQU5dE/TbixGGPzlu3TCODFFx; bm_sv=3F3AB4C8DC370B5D32956C52A635061B~YAAQLHhAF0c/V92GAQAAIlkSAhOTbV5HroQ3S9PgshkVv/JLZIzeXWZzp0trYgw7Z8f6qmG8fohIFaT1BGx5MWVXzBex4rSLNt4vWRQj70ArEnh2mauiDlafc6eST2k6JgxnnPcBp4ceAtu+l/7iLrnAqY0AhRIC1Ux3AZJjeX7JoLVN/PQ6Oags9NIowJtbXNo/D1TCdPx6pLGQ9ucHagfKI3AL1Bb4dWw4J+jqM0+NK7UEgq//f5bOgqPgRSw=~1',
    }

    params = {
        'email': email,
    }

    response = requests.get('https://signup.hulu.com/api/v3/accounts/status', params=params, cookies=cookies, headers=headers)

    html = response.text

    text = '"status":"existing"'

    if text in html:
        return f'true'
    else:
        return f'false'
