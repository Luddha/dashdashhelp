from django.db import models

# Create your models here.
class WG_VMS(models.Model):



class Wargames(models.Models):
    wg_name        = models.CharField(max_length=50)
    wg_file     = models.ForeignKey(WG_VMS, on_delete=models.CASCADE)
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
    wg_docs = models.ForeignKey(WG_WRITE_UP, on_delete=models.CASCADE)