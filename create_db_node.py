from register import *
import uuid
db.create_all()
dat = node(id=1,pub_id=str(uuid.uuid4()),nodename="test",encode_jwt="qwpeoiqpwoeipoqiwepoiqwe",ip="192.168.1.54")
db.session.add(dat)
db.session.commit()
