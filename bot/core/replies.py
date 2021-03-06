
class Reply:
    @staticmethod
    def not_in_game(user):
        return f'<@{user}>, не си в игра.'

    @staticmethod
    def used_50(player):
        return f'<@{player}>, използвал си 50:50.'

    @staticmethod
    def used_friend(player):
        return f'<@{player}>, използвал си помощ от приятел.'

    @staticmethod
    def used_audience(player):
        return f'<@{player}>, използвал си помощ от публиката.'

    @staticmethod
    def end_game(player, m):
        return f'<@{player}>, твоята игра приключи. Тръгваш си с - {m} лева.'

    @staticmethod
    def unknown_2_arg(player):
        return f'<@{player}>, не разпознат втори аргумент.'

    @staticmethod
    def no_yourself(player):
        return f'<@{player}>, не може да искаш помощ от себе си.'

    @staticmethod
    def no_player(player):
        return f'<@{player}>, не може да искаш помощ от потребител в игра.'

    @staticmethod
    def no_bot(player):
        return f'<@{player}>, не може да искаш помощ от бот.'

    @staticmethod
    def friend_help(helper, sec):
        return f'{helper}, имаш {sec} секунди да помогнеш на своят приятел.'

    @staticmethod
    def audience_help(sec):
        return f'Нека публиката се включи сега! Оставящи {sec} секунди.'

    @staticmethod
    def not_finished(player):
        return f'<@{player}>, все още не си приключил играта си.'

    @staticmethod
    def start_game(player):
        return f'<@{player}>, твоята игра започва сега!'

    @staticmethod
    def user_name(user, tag):
        return f'{user}#{tag}'

    @staticmethod
    def game_title(question_level, player, question_leva):
        return f'{question_level}. Играта на {player}. Въпрос за {question_leva} лева.'

    @staticmethod
    def question_added_by(author):
        return f"Въпрос добавен от {author}."

    @staticmethod
    def github_repo(stars, forks, issues):
        return f'ГитХъб репо. {stars} \u2b50 {forks} 🍴 {issues} \u2757'

    @staticmethod
    def first_place(place, name, count, what):
        return f'{place}. **{name}**🥇: {count} {what}'

    @staticmethod
    def sec_place(place, name, count, what):
        return f'{place}. **{name}**🥈: {count} {what}'

    @staticmethod
    def third_place(place, name, count, what):
        return f'{place}. **{name}**🥉: {count} {what}'

    @staticmethod
    def other_place(place, name, count, what):
        return f'{place}. **{name}**: {count} {what}'

    @staticmethod
    def system_info(node, sys, rel, cpu, ram):
        return f'{node}\n{sys} {rel}\n\
CPU usage: {cpu} % \n\
RAM usage: {ram} MiB'

    @staticmethod
    def choice(key, answer):
        return f'**{key}** {answer}'

    @staticmethod
    def total_votes(votes):
        return f"Общо гласoве: {votes}."

    @staticmethod
    def letter_percent(vote, percent):
        return f'{vote} {percent} %'

    @staticmethod
    def used_tech(python_version, discord_version):
        return f'''
Python {python_version} :snake:
discord.py rewrite branch {discord_version}
PyGithub
Pipenv
'''

    @staticmethod
    def game_of(player):
        return f'Играта на {player}.'

    @staticmethod
    def help_from_friend(player, helper, level):
        return f'Играта на {player}. Предложението на {helper} за въпрос {level}.'

    @staticmethod
    def help_from_audience(player, level):
        return f'Играта на {player}. Гласoве на публиката за въпрос {level}.'

    @staticmethod
    def list_general_commands(P):
        return f'**{P}инфо** - изпраща информация за бота.\n\
**{P}правила** - изпраща правилата на играта.\n\
**{P}команди** - изпраща всички команди с пояснение.\n\
**{P}добави** - изпраща информация как да добавиш въпрос.\n\
**{P}добавям** - ботът събира твоите въпроси (pin-нати съобщения в личния чат)\n\
**{P}форма** - ботът изпраща формата за въпроса.'

    @staticmethod
    def list_stat_commands(P):
        return f'**{P}топ10 автори** - изпраща класацията на потребителите с най-много добавени въпроси.\n\
**{P}топ10 играчи** - изпраща класацията на потребителите с най-много спечелени пари от игрите.'

    @staticmethod
    def list_game_commands(P):
        return f'**{P}игра** - стартира се нова игра за потребителя.\n\
**{P}[А, Б, В, Г]** - отговор на въпроса.\n\
**{P}50:50** - жокер, два грешни отговора се премахват.\n\
**{P}помощ [таг]** - жокер, 30 секунди се изчаква помощ от тагнатият.\n\
**{P}помощ публика** - жокери, 30 секунди се изчакват отговори в същият канал.\n\
**{P}жокери** - изпраща се илюстрация на наличните жокери.\n\
**{P}спирам** - играча се отказва от играта и се запазват парите от последният отговорен въпрос.'