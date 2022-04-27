from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=60, default='User')
    name = models.CharField(max_length=60)
    user_name = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    dob = models.DateField()
    country = models.CharField(max_length=50)
    def __str__(self):
        return {
            'user_id: '+str(self.user_id)+
            ' user_type'+ self.user_type+
            ' name '+ self.name+
            ' user_name '+ self.user_name+
            ' email '+ self.email+
            ' dob '+ str(self.dob)+
            ' country'+ self.country
        }

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    sign_in = models.DateTimeField(auto_now_add=True)
    sign_out = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    jwt = models.CharField(max_length=256)
    def __str__(self):
        return {
            'session_id': self.session_id,
            'sign_in': self.sign_in,
            'sign_out': self.sign_out,
            'user_id': self.user_id,
        }

class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=256, default='Name1')
    difficulty = models.CharField(max_length=60)
    duration = models.IntegerField(default=0)
    def __str__(self):
        return {
            'level_id': self.level_id,
            'song_name': self.song_name,
            'difficulty': self.difficulty,
            'duration': self.duration,
        }

class Attempt(models.Model):
    attempt_id = models.AutoField(primary_key=True)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return {
            'attempt_id': self.attempt_id,
            'level_id': self.level_id,
            'status': self.status,
            'user_id': self.user_id,
            'score': self.score
        }

class GameVariables(models.Model):
    variables_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lvl = models.IntegerField()
    video = models.IntegerField()
    Hs1 = models.IntegerField()
    Hs2 = models.IntegerField()
    Hs3 = models.IntegerField()
    FirstTime = models.IntegerField()
    score = models.IntegerField()
    def __str__(self):
        return {
            'variables_id': self.variables_id,
            'user_id': self.user_id,
            'lvl': self.lvl,
            'video': self.video,
            'Hs1': self.Hs1,
            'Hs2': self.Hs2,
            'Hs3': self.Hs3,
            'FirstTime': self.FirstTime,
            'score': self.score
        }