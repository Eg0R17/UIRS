def who_is_online(friends):
    activitie = {}
    for friend in friends:
        activitie.setdefault('away' if friend['status'] == 'online' and friend['last_activity'] > 10 else friend['status'], []).append(friend['username'])
    
    return activitie