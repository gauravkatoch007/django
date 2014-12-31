from django.db import models
from django.db.models.signals import *

# Create your models here.
class Person(models.Model):
    # info
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))

    #Relation
    parents = models.ManyToManyField('self', related_name='p', verbose_name="Parents", null=True, blank=True,
                                    symmetrical=False)
    children = models.ManyToManyField('self', related_name='c', verbose_name="Children", null=True, blank=True,
                                      symmetrical=False)


    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


# the 'connect_person' function will be called when Person m2m is changed.
def connect_person(sender, instance, action, reverse, model, pk_set, **kwargs):
    print "connect called with action '%s'" % action
    print instance.id

    if action == "pre_clear":

        for parent in instance.parents.all():
            print 'clear', parent.first_name
            # if remove bob as parent, then remove user from bobs children
            parent.children.remove(instance)


    if action == "post_add":

        for parent in instance.parents.all():
            print 'save', parent.first_name
            # when you add Bob as parent, them bob needs his list of children updated to match this.
            parent.children.add(instance)
            # when you add Bob as parent, them all bobs children need to have this user as there sibling.



m2m_changed.connect(connect_person, sender=Person.parents.through)