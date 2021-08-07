import telepot
import pprint
import urllib3
import pickle
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.loop import MessageLoop
from time import sleep
import random
bot = telepot.Bot('661805947:AAHAqZ9E73Y3awCA_s43VEZjteb0vhklla0')

hamkary={}
farhagi={}
trahi={}
jaize={}
tabligh={}
sport={}
pyam=[]
ktab=["http://s8.picofile.com/file/8352454942/photo_2019_02_16_07_19_16.jpg","چهار دهمین دوره مسابقات کتابخوانی : کنت مونت کریستو الکساندر دوما   / شگفتی آر .جی پلاسیو      تاریخ برگزاری:28 اسفند ماه سالن اجتماعات  مجتمع دینی صدر الاسلام"]
jok=["با سلام\nواحد دانشجویی معاونت اجتماعی شهرستان بندر خمیربه منظور حمایت، تقویت و ترويج فرهنگ و اخلاق علمي در جامعه، تقويت روحيه و بنيه علمي دانشجويان مستعد و توانمند و فراهم آوردن زمینه‌های مناسب برای فعاليت‌هاي جمعي علمي، همچنین بهره‌گیری از توانمندی و خلاقیت آنان در تحقق توسعه علمی و نهضت تولید علم و جنبش نرم‌افزاری دانشجویان حوزه‌هاي مختلف دانش با حمايت دانشگاهها ، دستگاه ها مرتبط و دیگر انجمن های فعال تشكيل شد و به فعاليت پرداخت. \nفعاليت‌هاي انجمن عبارتند از:\n1ـ مناظره و نقد علمي\n2ـ هم‌انديشي و نشست‌هاي تخصصي\n3ـ مطالعات و پژوهش‌هاي علمي\n4ـ نشر و ترويج يافته‌هاي علمي\n5ـ فعاليت‌هاي كمك آموزشي\n6- فعالیت های نیکوکاری\n7- جهت دهی دانشجویان متناسب با نیاز های جامعه\n8- ارتباط بین دانشجویان و سایر نهادها\n9- آسیب شناسی جامعه و ارائه راه حل\nبرخي از مصاديق و عرصه‌هاي فعاليت انجمن‌  عبارتند از:\n1ـ برگزاري دوره‌هاي آموزشي تكميلي و تقويتي و تشكيل كارگاههاي تخصصي\n2ـ برگزاري و همكاري در اجراي جشنواره‌ها، كنفرانس‌ها و مسابقات علمي \n3ـ توليد و انتشار نشريه علمي، كتاب و نشريات الكترونيكي،نرم‌افزارهاي رايانه‌اي و فيلم‌هاي علمي‌ـ آموزشي/n4ـ برنامه‌ريزي و اجراي بازديد‌هاي علمي از مراكز علمي، صنعتي و فناوري\n5ـ اطلاع‌رساني در خصوص كليه فعاليت‌هاي مرتبط با اهداف انجمن\n6ـ حمايت و تشويق مادي و معنوي از ابتكارات، خلاقيت‌هاي علمي، فعاليت‌هاي پژوهشي و اختراعات افراد مستعد/nاهداف تشكيل و فعاليت انجمن‌ عبارتند از:\n1ـ ايجاد زمينه‌هاي مناسب براي شكوفايي استعدادها، برانگيختن خلاقيت علمي دانشجويان، دانش‌آموختگان و بهره‌گيري از توانمندي ايشان در تقويت و تحقق فضاي علمي جامعه \n2ـ افزايش مشاركت و رقابت در فعاليت‌هاي علمي جمعي و نهادينه ساختن اين فعاليت‌ها  \n3ـ حمايت از فعاليت‌هاي علمي و راهنمايي و هدايت افراد در امر آموزش و پژوهش    \n4ـ تقويت و تحكيم پيوندهاي نظام آموزش عالي با بخش‌هاي مختلف جامع \n 5ـ تعميق دانش و بينش علمي با بهره‌گيري از توان علمي افراد متخصص"]
honary={}
nojavan={}
bozorgsal={}
user={}
win={}
admin=[22836135,119553655,198616120,174834698,124470512]

def telegram_webhook(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_id in admin:
        if content_type=="text":
            text = msg['text']
            user[chat_id]="start"
            if text=="/start":
                
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="members":
                a=len(hamkary.keys())
                bot.sendMessage(chat_id,str(a)+"تعداد اعضاء  دریافت کننده خبر")
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                         [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="/send":
                user[chat_id]="sendpyam"
                bot.sendMessage(chat_id,"شما در حال ارسال پيام مي باشيد لطفا پيام خود را تايپ کنيد")
                bot.sendMessage(chat_id,user[chat_id])
            elif text=="backup":
                file=open("khabar.txt","w")
                file.write(str(hamkary))
                file.close
                new_ba=list()
                for i in hamkary.keys():
                    new_ba.append(i)
                bot.sendMessage(chat_id,str(new_ba))
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))

            elif text=="comments":
                for i in pyam:
                    bot.sendMessage(chat_id,str(i))
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"),KeyboardButton(text="committees")],[KeyboardButton(text="delet_comments"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="delet_comments":
                pyam.clear()
                bot.sendMessage(chat_id,"نظر ها با موفقیت پاک شد")
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="committees":
                bot.sendMessage(chat_id, 'لطفا یکی از کمیته ها را جهت دریافت لیست درخواست همکاری انتخاب کنید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Cultural"), KeyboardButton(text="Designing")],[KeyboardButton(text="Advertising"),KeyboardButton(text="Sport")],[KeyboardButton(text="artistic"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="Cultural":
                
                new_Cultural=list()
                for t in farhagi.values():
                    new_Cultural.append(t)
                for e in new_Cultural:
                    bot.sendMessage(chat_id,str(e))
                bot.sendMessage(chat_id, 'لطفا یکی از کمیته ها را جهت دریافت لیست درخواست همکاری انتخاب کنید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Cultural"), KeyboardButton(text="Designing")],[KeyboardButton(text="Advertising"),KeyboardButton(text="Sport")],[KeyboardButton(text="artistic"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="Designing":
                
                new_Designing=list()
                for u in trahi.values():
                    new_Designing.append(u)
                for w in new_Designing:
                    bot.sendMessage(chat_id,str(w))
                bot.sendMessage(chat_id, 'لطفا یکی از کمیته ها را جهت دریافت لیست درخواست همکاری انتخاب کنید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Cultural"), KeyboardButton(text="Designing")],[KeyboardButton(text="Advertising"),KeyboardButton(text="Sport")],[KeyboardButton(text="artistic"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="Advertising":
                
                new_Advertising=list()
                for q in tabligh.values():
                    new_Advertising.append(q)
                for a in new_Advertising:
                    bot.sendMessage(chat_id,str(a))
                bot.sendMessage(chat_id, 'لطفا یکی از کمیته ها را جهت دریافت لیست درخواست همکاری انتخاب کنید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                       [KeyboardButton(text="Cultural"), KeyboardButton(text="Designing")],[KeyboardButton(text="Advertising"),KeyboardButton(text="Sport")],[KeyboardButton(text="artistic"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="Sport":
                
                new_sport=list()
                for r in sport.values():
                    new_sport.append(r)
                for v in new_sport:
                    bot.sendMessage(chat_id,str(v))
                bot.sendMessage(chat_id, 'لطفا یکی از کمیته ها را جهت دریافت لیست درخواست همکاری انتخاب کنید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                       [KeyboardButton(text="Cultural"), KeyboardButton(text="Designing")],[KeyboardButton(text="Advertising"),KeyboardButton(text="Sport")],[KeyboardButton(text="artistic"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="artistic":
                
                new_artistic=list()
                for r in honary.values():
                    new_artistic.append(r)
                for v in new_artistic:
                    bot.sendMessage(chat_id,str(v))
                bot.sendMessage(chat_id, 'لطفا یکی از کمیته ها را جهت دریافت لیست درخواست همکاری انتخاب کنید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                       [KeyboardButton(text="Cultural"), KeyboardButton(text="Designing")],[KeyboardButton(text="Advertising"),KeyboardButton(text="Sport")],[KeyboardButton(text="artistic"),KeyboardButton(text="comeback")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="comeback":
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="/drawing":
                new_list=[]
                for i in jaize.keys():
                    new_list.append(i)
                a=len(new_list)-1
                for t in range(10):
                    b=random.randint(0,a)
                    user_win=new_list[b]
                    user[user_win]="win"
                    bot.sendMessage(chat_id,str(user_win)+ user[user_win])
                    bot.sendMessage(user_win,"شما برنده قرعه کشی جشن کمیته دانشجویی شده اید لطفا شماره تماس ومشخصات خود را  برای ما در یک خط ارسال فرمایید.")
                    bot.sendMessage(user_win,"نام ونام خانوادگی -شماره تماس")
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="winr":
                for i in win.keys():
                    bot.sendMessage(chat_id,win[i][:-4]+"****" )
            elif text=="/win":
                    for i in win.keys():
                        bot.sendMessage(chat_id,win[i])
            elif text=="/admin":
                user[chat_id]="admin"
                bot.sendMessage(chat_id,"ok please enter chat id admin:")
            elif text=="send":
                i="شما در 14 امین دوره مسابقه کتابخوانی به صورت آنلاین شرکت کرده اید لذا با . وارد کردن کد دریافتی از بات می توانید از طریق لینک زیر در مسابقه شرکت نمایید."
                for p in nojavan.keys():
                    bot.sendMessage(p,i)
                    bot.sendMessage(p,"http://daneshjooyankhamir.ir/book/")
                for p in bozorgsal.keys():
                    bot.sendMessage(p,i)
                    bot.sendMessage(p,"http://daneshjooyankhamir.ir/book/")
                bot.sendMessage(chat_id, 'سلام ،شما به عنوان ادمین انتخاب شده اید،لطفان به نکات که به آن اشاره شده پایبند باشید.1 ارسال هر گونه بات از  طرف شما باع ارسال آن پیام به همه اعضاء بات می باشد.جهت انجام سایر کار  از گزینه های تعریف شده استفاده نمایید',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="members"), KeyboardButton(text="backup")],[KeyboardButton(text="committees"),KeyboardButton(text="comments")],[KeyboardButton(text="send")]
                                    ]
                                ,resize_keyboard=True))
            elif text=="book":
                bot.sendMessage(chat_id,str(nojavan))
                bot.sendMessage(chat_id,str(bozorgsal)) 
            elif text=="delet_book":
                nojavan.clear()
                bozorgsal.clear()
                bot.sendMessage(chat_id,"لیست شرکت کنندگان پاک شد")
            
            else:
                if user[chat_id]=="admin":
                    user_admin=int(text)
                    admin.append(user_admin)
                    file=open("admin.txt","w")
                    file.write(str(admin))
                    file.close
                    bot.sendMessage(chat_id,"ادمین با موفقیت ثبت شد")
                    bot.sendMessage(user_admin,"از این پش ما ادمین بات خواهید بود لطفا بات را دوباره استارت کنید")
                else:
                    for p in hamkary.keys():
                        bot.sendMessage(p,text)
        elif content_type=="photo":
            photo = msg['photo'][-1]["file_id"]
            for p in hamkary.keys():
                bot.sendPhoto(p,photo)
        elif content_type=="video":
            video0 = msg['video']['file_id']
            
            for p in hamkary.keys():
                bot.sendVideo(p,video)      

    else:
        text = msg['text']
        if text=="/start":
             user[chat_id]="start"
             jaize[chat_id]=chat_id
             bot.sendMessage(chat_id, 'لطفا یکی از گزینه های زیر را انتخاب نمایید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="دریافت خبرنامه"), KeyboardButton(text="مسابقه کتابخوانی")],[KeyboardButton(text="درباره ما"),KeyboardButton(text="ارتباط با ما")],[KeyboardButton(text="همکاری با ما")]
                                ]
                            ,resize_keyboard=True))
        elif text=="دریافت خبرنامه":
             if chat_id not in hamkary.keys():
                hamkary[chat_id]=chat_id
                bot.sendMessage(chat_id, 'با تشکر از شما \n از این پس اخبار واطلاعیه های کمیته از این طریق به اطلاع شما خواهد رسید',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="دریافت خبرنامه"), KeyboardButton(text="مسابقه کتابخوانی")],[KeyboardButton(text="درباره ما"),KeyboardButton(text="ارتباط با ما")],[KeyboardButton(text="همکاری با ما")]
                                ]
                            ,resize_keyboard=True))
             else:
                bot.sendMessage(chat_id,"شما قبلا در  لیست دریافت کنندگان خبرنامه قرار گرفته اید\n لطفا یکی از گزینه های زیر را انتخاب کنید.")
        elif text=="مسابقه کتابخوانی":
             bot.sendMessage(chat_id, 'لطفا یکی از گزینه های زیر را انتخاب کنید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="شرکت در مسابقه"),KeyboardButton(text="هدف مسابقه")],[KeyboardButton(text="معرفی کتاب"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="شرکت در مسابقه":
             bot.sendMessage(chat_id, 'لطفا یکی از  دو رده سنی زیر را جهت شرکت در مسابقه آنلاین انتخاب نمایید',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="12 تا 18 سال"),KeyboardButton(text="18 سال به بالا")],[KeyboardButton(text="مسابقه کتابخوانی")]
                                ]
                            ,resize_keyboard=True))
        elif text=="12 تا 18 سال":
             token="141218"+str(chat_id)
             nojavan[chat_id]=token
             file=open("nojavan.txt","w")
             file.write(str(nojavan))
             file.close
             new_Cultural=list()
             bot.sendMessage(chat_id,token+"\n"+"کد شرکت در مسابقه")
             bot.sendMessage(chat_id, 'شما در 14 همین دوره مسابقه کتابخوانی شرکت کرده اید در تاریخ مورد نظر به لینک که برای شما ارسال خواهد شد مراجعه کنید',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="شرکت در مسابقه"),KeyboardButton(text="هدف مسابقه")],[KeyboardButton(text="معرفی کتاب"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="18 سال به بالا":
             token="1418"+str(chat_id)
             bozorgsal[chat_id]=token
             file=open("bozorgsal.txt","w")
             file.write(str(bozorgsal))
             file.close
             new_Cultural=list()
             bot.sendMessage(chat_id,token+"\n"+"کد شرکت در مسابقه")
             bot.sendMessage(chat_id, 'شما در 14 همین دوره مسابقه کتابخوانی شرکت کرده اید در تاریخ مورد نظر به لینک که برای شما ارسال خواهد شد مراجعه کنید',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="شرکت در مسابقه"),KeyboardButton(text="هدف مسابقه")],[KeyboardButton(text="معرفی کتاب"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="هدف مسابقه":
             bot.sendMessage(chat_id, 'هدف از مسابقه کتابخوانی: ترویج فرهنگ کتاب و کتاب خوانی و سوق دادن جامعه بندر خمیر به سمت فعالیت های فرهنگی و کتابخوانی ، بالا بردن سطح فرهنگ مردم و تغییر نگاه و دید مردم به زندگی و جامعه ؛ بالا بردن سطح علمی مردم \nدر پاراف : شهر خمیر بسیار از لحاظ علمی ضعیف است ، با وجود اینکه از فرهنگ غنی برخورداره ، بدلیل مجاورت با دریا و شرایط اقلیمی منطقه جنوب که روی معیشت و ازدواج و ... مردم تاثیر زیادی داره',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="شرکت در مسابقه"),KeyboardButton(text="هدف مسابقه")],[KeyboardButton(text="معرفی کتاب"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="معرفی کتاب":
             bot.sendPhoto(chat_id,str(ktab[-2]))
             bot.sendMessage(chat_id,"لطفا یکی از گزینه های زیر را انتخاب نمایید.",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="شرکت در مسابقه"),KeyboardButton(text="هدف مسابقه")],[KeyboardButton(text="معرفی کتاب"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="درباره ما":
             bot.sendMessage(chat_id, 'گزینه مورد نظر را انتخاب کنید',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                     [ KeyboardButton(text="اهداف ما"),KeyboardButton(text="دریافت گزارش کار به صورت PDF")],[KeyboardButton(text="دریافت گزارش کار به صورت ویدیو"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="اهداف ما":
             bot.sendMessage(chat_id,str(jok[0]),
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="اهداف ما"),KeyboardButton(text="دریافت گزارش کار به صورت PDF")],[KeyboardButton(text="دریافت گزارش کار به صورت ویدیو"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="دریافت گزارش کار به صورت PDF":
             bot.sendDocument(chat_id,"BQADBAAD8QQAAnjTSFPXtzzn5UjAoQI")   
             bot.sendMessage(chat_id,"لطفا یکی از گزینه هارا انتخاب کنید",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                     [ KeyboardButton(text="اهداف ما"),KeyboardButton(text="دریافت گزارش کار به صورت PDF")],[KeyboardButton(text="دریافت گزارش کار به صورت ویدیو"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="دریافت گزارش کار به صورت ویدیو":
             bot.sendVideo(chat_id,"BAADBAADDgQAAnk4OVNKCIa4VKrgtAI")
             bot.sendMessage(chat_id,"لطفا یکی از گزینه هارا انتخاب کنید",
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="اهداف ما"),KeyboardButton(text="دریافت گزارش کار به صورت PDF")],[KeyboardButton(text="دریافت گزارش کار به صورت ویدیو"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="ارتباط با ما":
             bot.sendMessage(chat_id, 'لطفا یکی از گزینه های زیر را جهت ارتباط با انتخاب نمایید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="ارسال پیام"),KeyboardButton(text="instagram")],[KeyboardButton(text="تماس"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="ارسال پیام":
             user[chat_id]="nazar"
             bot.sendMessage(chat_id, 'پیام شما بدون مشخصات  ارسال خواهد شد در صورت لزوم اطلاعات خود را ذکر کنید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                     [ KeyboardButton(text="ارسال پیام"),KeyboardButton(text="instagram")],[KeyboardButton(text="تماس"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="instagram":
             bot.sendMessage(chat_id, "https://www.instagram.com/daneshjooyankhamir/")
             bot.sendMessage(chat_id, 'لطفا یکی از گزینه های زیر را جهت ارتباط با انتخاب نمایید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [ KeyboardButton(text="ارسال پیام"),KeyboardButton(text="instagram")],[KeyboardButton(text="تماس"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="تماس":
             bot.sendContact(chat_id,"09909269531","کمیته دانشجویی صدر الاسلام بندرخمیر")
             bot.sendMessage(chat_id, 'لطفا یکی از گزینه های زیر را جهت ارتباط با انتخاب نمایید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                     [ KeyboardButton(text="ارسال پیام"),KeyboardButton(text="instagram")],[KeyboardButton(text="تماس"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="بازگشت":
             user[chat_id]="start"
             bot.sendMessage(chat_id, 'لطفا یکی از گزینه های زیر را انتخاب کنید.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="دریافت خبرنامه"), KeyboardButton(text="مسابقه کتابخوانی")],[KeyboardButton(text="درباره ما"),KeyboardButton(text="ارتباط با ما")],[KeyboardButton(text="همکاری با ما")]
                                ]
                            ,resize_keyboard=True))
        elif text=="همکاری با ما":
             bot.sendMessage(chat_id, 'لطفا هر یک از کمیته های که تمایل به همکاری دارید را انتخاب کنید',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="فرهنگی"), KeyboardButton(text="طراحی")],[KeyboardButton(text="تبلیغات"),KeyboardButton(text="ورزشی")],[KeyboardButton(text="هنری"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="فرهنگی":
             user[chat_id]="farhangi"
             bot.sendMessage(chat_id,"لطفا جهت همکاری با کمیته فرهنگی  مشخصات خود را به صورت  فرمت خواسته شده ارسال نمایید.")
             bot.sendMessage(chat_id, 'نام- نام خانوادگی- شماره تماس ',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="فرهنگی"), KeyboardButton(text="طراحی")],[KeyboardButton(text="تبلیغات"),KeyboardButton(text="ورزشی")],[KeyboardButton(text="هنری"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="طراحی":
             user[chat_id]="trahi"
             bot.sendMessage(chat_id,"لطفا جهت همکاری با کمیته طراحی مشخصات خود را به صورت فرمت خواسته شده ارسال نمایید")
             bot.sendMessage(chat_id, 'نام- نام خانوادگی- شماره تماس  ',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="فرهنگی"), KeyboardButton(text="طراحی")],[KeyboardButton(text="تبلیغات"),KeyboardButton(text="ورزشی")],[KeyboardButton(text="هنری"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="تبلیغات":
             user[chat_id]="tablighat"
             bot.sendMessage(chat_id,"لطفا جهت همکاری با کمیته تبلیغات مشخصات خود را به صورت فرمت خواسته شده ارسال نمایید")
             bot.sendMessage(chat_id, 'نام- نام خانوادگی- شماره تماس ',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="فرهنگی"), KeyboardButton(text="طراحی")],[KeyboardButton(text="تبلیغات"),KeyboardButton(text="ورزشی")],[KeyboardButton(text="هنری"),KeyboardButton(text="بازگشت")]
                                ]
                            ,resize_keyboard=True))
        elif text=="ورزشی":
             user[chat_id]="sport"
             bot.sendMessage(chat_id,"لطفا جهت همکاری با کمیته ورزشی مشخصات خود را به صورت فرمت خواسته شده ارسال نمایید")
             bot.sendMessage(chat_id, 'نام- نام خانوادگی- شماره تماس ',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="فرهنگی"), KeyboardButton(text="طراحی")],[KeyboardButton(text="تبلیغات"),KeyboardButton(text="ورزشی")],[KeyboardButton(text="هنری"),KeyboardButton(text="بازگشت")]
                            ],resize_keyboard=True))
        elif text=="هنری":
             user[chat_id]="honary"
             bot.sendMessage(chat_id,"لطفا جهت همکاری با کمیته هنری مشخصات خود را به صورت فرمت خواسته شده ارسال نمایید")
             bot.sendMessage(chat_id, 'نام- نام خانوادگی- شماره تماس  ',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="فرهنگی"), KeyboardButton(text="طراحی")],[KeyboardButton(text="تبلیغات"),KeyboardButton(text="ورزشی")],[KeyboardButton(text="هنری"),KeyboardButton(text="بازگشت")]
                            ],resize_keyboard=True))
            
        else:
            if user[chat_id]=="farhangi":
                if chat_id not in farhagi.keys():
                    farhagi[chat_id]=text
                    file=open("farhangi.txt","w+")
                    file.write(str(farhagi))
                    file.close
                    bot.sendMessage(chat_id, 'مشخصات شما جهت همکاری با کمیته فرهنگی ثبت شد.در اسرع وقت با شما تماس گرفته خواهد شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
                           
                else:
                    bot.sendMessage(chat_id, 'مشخصات شما قبلا ذخیره شده است.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            elif user[chat_id]=="trahi":
                if chat_id not in trahi.keys(): 
                    trahi[chat_id]=text
                    file=open("trahi.txt","w+")
                    file.write(str(trahi))
                    file.close
            #bot.sendMessage(chat_id,str(trahi[chat_id]))
                    bot.sendMessage(chat_id, 'مشخصات شما جهت همکاری با کمیته طراحی ثبت شد.در اسرع وقت با شما تماس گرفته خواهد شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
                else:
                    bot.sendMessage(chat_id, 'مشخصات شما قبلا ذخیره شده است.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            elif user[chat_id]=="tablighat":
                if chat_id not in tabligh.keys():
                    tabligh[chat_id]=text
                    file=open("tablighat.txt","w+")
                    file.write(str(tabligh))
                    file.close
            #bot.sendMessage(chat_id,str(tabligh[chat_id]))
                    bot.sendMessage(chat_id, 'مشخصات شما جهت همکاری با کمیته تبلیغات ثبت شد.در اسرع وقت با شما تماس گرفته خواهد شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
                else:
                    bot.sendMessage(chat_id, 'مشخصات شما قبلا ذخیره شده است.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            elif user[chat_id]=="sport":
                if chat_id not in sport.keys():
                    sport[chat_id]=text
                    file=open("sport.txt","w+")
                    file.write(str(sport))
                    file.close
            #bot.sendMessage(chat_id,str(sport[chat_id]))
                    bot.sendMessage(chat_id, 'مشخصات شما جهت همکاری با کمیته ورزشی ثبت شد.در اسرع وقت با شما تماس گرفته خواهد شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
                else:
                    bot.sendMessage(chat_id, 'مشخصات شما قبلا ذخیره شده است.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            elif user[chat_id]=="honary":
                if chat_id not in honary.keys(): 
                    honary[chat_id]=text
                    file=open("honary.txt","w+")
                    file.write(str(honary))
                    file.close
            #bot.sendMessage(chat_id,str(sport[chat_id]))
                    bot.sendMessage(chat_id, 'مشخصات شما جهت همکاری با کمیته هنری ثبت شد.در اسرع وقت با شما تماس گرفته خواهد شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
                else:
                    bot.sendMessage(chat_id, 'مشخصات شما قبلا ذخیره شده است.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            elif user[chat_id]=="nazar":
                pyam.append(text)
                bot.sendMessage(chat_id, 'پیام شما با موفقیت ارسال شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            elif user[chat_id]=="win":
                win[chat_id]=text
                bot.sendMessage(chat_id, 'مشخصات شما جز برندگان ثبت شد.',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            else:
                bot.sendMessage(chat_id, 'گزینه مورد نر تعریف نشده است',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                   [ KeyboardButton(text="بازگشت")]
                               ]
                           ,resize_keyboard=True))
            
    return "OK"




MessageLoop(bot,telegram_webhook).run_as_thread()
while 1:
    sleep(20)