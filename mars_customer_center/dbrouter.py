class Router:
    def db_for_read(self, model, **hints):
        return 'db_slave'

    def db_for_write(self, model, **hints):
        return 'default'
