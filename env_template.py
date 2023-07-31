username = "your_username"
password = "your_password"
host = "the_host"

def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'