from django.db import models

# Create your models here.
class WG_VMS(models.Model):
    wg_vm_name = models.CharField(max_length=50)
    wg_vm_file = models.FileField()


class WG_DOCS(models.Model):
    wg_doc_title = models.CharField(max_length=50)
    wg_doc_body  = models.TextField()
    wg_doc_time  = models.TimeField()



class Wargames(models.Model):
    wg_name     = models.CharField(max_length=50)
    wg_file     = models.ForeignKey(WG_VMS, on_delete=models.CASCADE, blank=True, null=True)
    NOT_STARTED = "NS"
    STARTED     = "ST"
    PAUSED      = "PA"
    DONE        = "DO"
    wg_options  = (
        (NOT_STARTED, "Not Started"),
        (STARTED,     "Started"    ),
        (PAUSED,      "Paused"     ),
        (DONE,        "Done"       )
    )
    wg_status = models.CharField(max_length=2, choices=wg_options, default=NOT_STARTED)
    wg_doc = models.ForeignKey(WG_DOCS, on_delete=models.CASCADE, blank=True, null=True)

