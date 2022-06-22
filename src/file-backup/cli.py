from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination=values
        namespace.driver = driver.lower()
        namespace.destination = destination




def create_parser():
    parser = ArgumentParser(description="""
    Back up material to local or aws s3 or google buick
    """)

    parser.add_argument("path", help="Relative path of file to backup")
    parser.add_argument("--driver",
            help="how & where to store file",
            nargs=2,
            action=DriverAction,
            required=True)


    return parser