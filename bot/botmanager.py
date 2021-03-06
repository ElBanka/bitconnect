from .botrepository import BotRepository


class BotManager:
    bot_repo = None

    def __init__(self):
        self.bot_repo = BotRepository()

    def get_bot(self, id):
        """
        Retrieve a bot from database by id
        :param id:
        :return Bot:
        """
        return self.bot_repo.get(id)

    def get_bots(self, search_criteria):
        """
        Retrieve bots from database
        :return Bot[]:
        """
        return self.bot_repo.getList(search_criteria=search_criteria)

    def print_bot(self, bot):
        """
        Print Bot info
        :param bot:
        """
        print(bot.get_id())

    def list_bots(self, search_criteria):
        """
        List all bots or one bot if -id option is given
        """
        bots = self.get_bots(search_criteria)
        for bot in bots:
            self.print_bot(bot)

    def create_bot(self, bot_type, threshold, win_limit, loss_limit, amount):
        """
        Create a new bot in the database
        :param amount:
        :param loss_limit:
        :param win_limit:
        :param threshold:
        :param bot_type:
        :return Bot:
        """
        if not bot_type or not threshold or not win_limit or not loss_limit or not amount:
            raise Exception("All data must be given")
        else:
            return self.bot_repo.create(bot_type, threshold, win_limit, loss_limit, amount)

    def delete_bot(self, bot_id):
        """
        Delete an existing bot from the database
        :param bot_id:
        :return:
        """
        if bot_id:
            self.bot_repo.delete(bot_id)
        else:
            raise Exception("No bot_id found for deleting bot.")