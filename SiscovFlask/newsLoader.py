from sqlalchemy.sql.expression import false, true
from news import noticias
from models import Noticias, noticias_municipio, noticias_estado, db

def existNews(news_id):
    state = Noticias.query.filter_by(id=news_id).first()    
    if not state:
        return false
    return true

if __name__ == '__main__':
    for key, value in noticias.items():
        print("Inserting News...")
        for news in value:
            estado_id = news['estado_id']
            
            news_already_exist = existNews(news['id'])

            if news_already_exist == false:
                news_to_be_created = Noticias(id = news['id'], url=news['url'])
                db.session.add(news_to_be_created)
                db.session.commit()

                db.session.execute(noticias_estado.insert(), params={
                    "noticia_id": news['id'],
                    "estado_id": estado_id},)

                if news['municipio_id']:
                    for municipio in news['municipio_id']:
                        db.session.execute(noticias_municipio.insert(), params={
                            "noticia_id": news['id'],
                            "municipio_id": municipio},)
                
                db.session.commit()
        print("{} News Sucessfully inserted!".format(key))