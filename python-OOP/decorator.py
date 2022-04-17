from datetime import datetime

def format_report(report):
    def inner(text):
        print('A report')
        print('-' * 50)
        report(text)
        print('-' * 50)
        print('Report completed: {}.'.format(datetime.now()))
    return inner

@format_report
def report(text):
    print(text)


# report = format_report(report)

report('creating a report using decorator.')