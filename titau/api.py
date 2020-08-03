from titau import app, db, model
from flask_restx import Api, Resource

api = Api(app, title='tItau', description='AirbNb Consulting')

@api.route('/residencias', methods=['POST','GET'])
@api.route('/residencias/<string:campo>/<string:valor>', methods=['GET'])
class Residencia(Resource):
    def get(self, campo='', valor=''):
        if campo != '' and valor=='':
            return {'msg': f'Valor do {campo} necessario'}, 500
        permitidos = [
            'name',
            'host_name',
            'neighbourhood',
            'room_type',
            'neighbourhood_group',
            ''
        ]
        if campo not in permitidos:
            return {'msg': f'Campo *{campo}* nao pode ser pesquisado'}, 500
            
        if campo != '':
            cond = {campo: valor}
            regs = model.Residencia.query.filter_by(**cond)
        else:
            regs = model.Residencia.query.all()
        ret = []
        for r in regs:
            ret.append(r.dict())
            
        return ret, 200

    def post(self):
        l = model.Like()
        l.residencia_id = request.form['id']
        db.add(l)
        db.commit()
        return {'msg':'Like salvo'}, 200

@api.route('/preco-medio/')
@api.route('/preco-medio/<string:campo>/<string:valor>')
class Media(Resource):
    def get(self, campo='', valor=''):
        if campo != '' and valor=='':
            return {'msg': f'Valor do {campo} necessario'}, 500

        permitidos = [
            'room_type',
            'neighbourhood_group',
            ''
        ]
        if campo not in permitidos and campo != '':
            return {'msg': f'Campo *{campo}* nao pode ser pesquisado'}, 500
            
        if campo != '':
            cond = {campo: valor}
            regs = model.Media.query.filter_by(**cond)
        else:
            regs = model.Media.query.all()
        ret = []
        for r in regs:
            ret.append(r.dict())
            
        return ret, 200
