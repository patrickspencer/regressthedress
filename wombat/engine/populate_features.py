from wombat.models import dbsession, ItemFeature

f = open('key_words.txt', 'r')
key_words = f.read().split("\n") 
f.close() # close file

def get_or_create(f):
    instance = dbsession.query(ItemFeature).filter(ItemFeature.name == f, ItemFeature.category == 1).first()
    if instance:
        return instance, False
    else:
        instance = ItemFeature(
                name = f,
                category = 1,
        )
        dbsession.add(instance)
        dbsession.commit()
        return instance, True

banned_list = ['']
for word in key_words:
    if word not in '':
        get_or_create(f = word)

features = dbsession.query(ItemFeature).filter(ItemFeature.category == 1).all()

for feature in features:
    print(feature.name)
