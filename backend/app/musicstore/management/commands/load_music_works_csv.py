import os, csv
from django.core.management.base import BaseCommand, CommandError
from musicstore.models import MusicWork


class Command(BaseCommand):
    help = "Loading data from csv-like files"

    def add_arguments(self, parser):
        parser.add_argument('load_file')

    def handle(self, *args, **options):
        load_file = options.get('load_file', None)
        if load_file:
            f_path = f"/code/app/media/work_files/{load_file}"
            with open(f_path, 'r') as f:
                red = csv.DictReader(f)
                for r in red:
                    self.stdout.write("step-1")
                    res = True
                    if r.get('iswc'):
                        self.stdout.write("step-2")
                        res = self.update_by_iswc(r.get('iswc'), r, res)
                        res = self.check_without_iswc(r.get('iswc'), r, res)
                        self.add_work(r.get('iswc'), r, res)
                        self.stdout.write("step-2 end")
                    else:
                        self.stdout.write("step-2a")
                        res = self.check_without_iswc(r.get('iswc'), r, res)
                        self.add_work(r.get('iswc'), r, res)
                        self.stdout.write("step-2a end")
                self.stdout.write("File is closed")

    def obj_update(self, object, data):
        object.iswc = data.get('iswc')
        object.title = data.get('title')
        object.contributors = list(set(object.contributors + data.get('contributors').split('|')))
        object.save()

    def check_without_iswc(self, iswc, data, res):
        self.stdout.write("check_without_iswc is started")
        if res:
            work_object = MusicWork.objects.filter(
                iswc = None,
                title = data.get('title'),
                contributors__contains = data.get('contributors').split('|')
            ).first()
            if work_object:
                self.obj_update(work_object, data)
                res = False
        else:
            pass
        return res


    def update_by_iswc(self, iswc, data, res):
        self.stdout.write("update_by_iswc is started")
        if res:
            work_object = MusicWork.objects.filter(iswc=iswc).first()
            if work_object:
                self.obj_update(work_object, data)
                res = False
        else:
            pass
        return res


    def add_work(self, iswc, data, res):
        self.stdout.write("add_work is started")
        if res:
            MusicWork.objects.create(
                iswc = iswc,
                title = data.get('title'),
                contributors = data.get('contributors').split('|')
            )
        else:
            pass
