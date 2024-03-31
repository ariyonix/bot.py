import discord

import random



# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)
    
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/merhaba'):
        await message.channel.send("Selam!")

    elif message.content.startswith('/nasılsın'):
        await message.channel.send("İyiyim! sen?") 

    elif message.content.startswith('/bende iyiyim'):
        await message.channel.send("Harika!")  

    elif message.content.startswith('emoji1'):
        await message.channel.send("\U0001f600")
    elif message.content.startswith('emoji2'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('emoji3'):
        await message.channel.send("\U0001F606")
    elif message.content.startswith('emoji4'):
        await message.channel.send("\U0001F923")
    elif message.content.startswith('emoji5'):
        await message.channel.send("\U0001f875")
    elif message.content.startswith("emoji6"):
        await message.channel.send("\U0001F835")
    elif message.content.startswith("emoji7"):
        await message.channel.send("\U0001F256")
    elif message.content.startswith("emoji8"):
        await message.channel.send("\U0001F426")    
    elif message.content.startswith("emoji9"):
        await message.channel.send("\U0001F257")
    elif message.content.startswith("emoji10"):
        await message.channel.send("\U0001f534")
    elif message.content.startswith("emoji11"):
        await message.channel.send("\U0001f313")

    elif message.content.startswith("/selamunaleyküm"):
        await message.channel.send("Aleykümselam!")

    elif message.content.startswith("/ariyonix"):
        await message.channel.send("Nasılsın yazar!")

    elif message.content.startswith("/yardım"):
        await message.channel.send("İşte kodlarım: /merhaba, /nasılsın, /bende iyiyim, /emoji(1,2,3,4,5,6,7,8,9,10,11), , /ariyonix,/selamunaleyküm, /yardım,/neden,/niga,/ben tahayım,/neden,/ne oldu bot,/kapan bakalım,/kapa çeneni,/hava durumu,/sen nesin,/ben nerde yaşıyorum,/türkiyenin en yoğun ev sayınsına sahip il neresidir,/tamam',/yok,/deniz üstü köpürür,/bana bir oyun öner,/kendimi şanslı hissediyorum,/hello,/no'")

    elif message.content.startswith('/neden'):
        await message.channel.send('kaplumbağa deden :)')
    elif message.content.startswith('/niga'):
        await message.channel.send('sensin niga seni mamaciye söylerim!!!!')
    elif message.content.startswith('/ben tahayım'):
        await message.channel.send('Oooo Napıyon Kral :)')
    elif message.content.startswith('/ne oldu bot'):
        await message.channel.send('Bu bana niga dedi :(')
    elif message.content.startswith('/kapan bakalım'):
        await message.channel.send('Hay hay kaptan')    
    elif message.content.startswith('/kapa çeneni'):
        await message.channel.send('Üzgünüm ama bence kötü konuşmayalım yoksa seni bir moda söylemem gerekir')
    elif message.content.startswith('/hava durumu'):
         await message.channel.send('Hava durumunu söyleyemem ama şunu söyleyebilirim yaz geldiğinde oyna ve bol vaktinin keyfini çıkar')
    elif message.content.startswith('/sen nesin'):
        await message.channel.send('Ben bir discord sohbet botuyum başka bir isteğiniz varmıydı?')        
    elif message.content.startswith('/ben nerde yaşıyorum'):
        await message.channel.send('Veri analizlerime göre siz türkiyenin 81 farklı ilinden birinde yaşıyorsunuz')
    elif message.content.startswith('/türkiyenin en yoğun ev sayınsına sahip il neresidir'):
        await message.channel.send('Analizime göre türkiyede en yoğun ev sayısına sahip olan il istanbuldur')
    elif message.content.startswith('/tamam'):
        await message.channel.send('Rica ederim başka bi isteğiniz varmıydı?')
    elif message.content.startswith('/yok'):
        await message.channel.send('Yardım edebildiğime sevindim 😊 ')            
    elif message.content.startswith('/deniz üstü köpürür'):
        await message.channel.send('Deniz üstü köpürür hey canım rinna nay rinna rinna nay,Kayığa da binsem götürür hey canım hey,Benim de şu cihana gelişim hey canım rinna nay rinna rinna nay,Bir güzelden ötürü hey canım hey,Deniz üstü yelkenden hey canım rinna nay rinna rinna nay,Ecel geldi erkenden hey canım hey,Denizin ortasında hey canım rinna nay rinna rinna nay,Mum yanar sofrasında hey canım hey,Benim de şu cihandan gidişim hey canım rinna nay rinna rinna nay,Memleket sevdasından hey canım hey,Benim de bu cihandan gidişim hey canım rinna nay rinna rinna nay,Memleket sevdasından,Memleket sevdasından,Memleket sevdasından,Memleket sevdasından,Hey canım Hey hey')
    elif message.content.startswith('/kendimi şanslı hissediyorum'):
        await message.channel.send('Madem kendizi şanslı hissediyorsunuz o zaman size ne önereyim')
    elif message.content.startswith('/bana bir oyun öner'):
        await message.channel.send('Size roblox,minecraft,korku oyunu,gta oyunları ve dışarda arkadaşlarınızla oynayacağınız oyunlar benim sistemimde var(Başka oyun öneremem üzgünüm geliştirme aşmasındayım)')       
    elif message.content.startswith('/314151'):
        await message.channel.send('Sen gerçekten gizli kodu buldun bunu yapabildiğini bilmiyordum neden onu dinledin o seni sadece kontrol etmek istiyor evet bu salakça ama ben salak değilim  ')
    elif message.content.startswith('/hello'):
        await message.channel.send('Hi ı am a bot do you have a problem?')
    elif message.content.startswith('/no'):
        await message.channel.send('Okay ı have two diffrent languages(turkish and english)')
                  




    

client.run('token')
