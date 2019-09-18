from create_db import *
import uuid
db.create_all()
dat = node(id=1,pub_id=str(uuid.uuid4()),nodename="test",encode_jwt="qwpeoiqpwoeipoqiwepoiqwe",admin=False)
db.session.add(dat)
db.session.commit()
