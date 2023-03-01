import json

from odoo.http import route, request, Response, Controller


class KedatechMaterialController(Controller):
    @route('/kedatech/material', auth='user', type='http', methods=['GET'])
    def get_list_material(self):
        data = []
        materials = request.env['kedatech.material'].search([])

        for material in materials:
            entry = {
                'id': material.id,
                'name': material.name,
                'code': material.code,
                'material_type': material.material_type,
                'buy_price': material.buy_price,
                'supplier': {
                    'id': material.supplier.id,
                    'name': material.supplier.name
                }
            }

            data.append(entry)

        result = {
            'data': data
        }

        return Response(json.dumps(result), mimetype='application/json')

    @route('/kedatech/material/create', auth='user', type='http', methods=['POST'], csrf=False)
    def create_material(self):
        body = request.httprequest.json

        material = request.env['kedatech.material'].create(body)
        
        data = {
            'id': material.id,
            'name': material.name,
            'code': material.code,
            'material_type': material.material_type,
            'buy_price': material.buy_price,
            'supplier': {
                'id': material.supplier.id,
                'name': material.supplier.name
            }
        }

        result = {
            'data': data
        }

        return Response(json.dumps(result), mimetype='application/json')

    @route('/kedatech/material/update', auth='user', type='http', methods=['POST'], csrf=False)
    def update_material(self):
        body = request.httprequest.json
        result = {'error': ''}

        _id = body.get('id')
        if not _id:
            result.update({'error': 'No material id to be updated found'})

        material = request.env['kedatech.material'].browse([_id])
        material.write(body)
        
        data = {
            'id': material.id,
            'name': material.name,
            'code': material.code,
            'material_type': material.material_type,
            'buy_price': material.buy_price,
            'supplier': {
                'id': material.supplier.id,
                'name': material.supplier.name
            }
        }

        result.update({'data': data})
        status = 200 if not result['error'] else 404

        return Response(json.dumps(result), status=status, mimetype='application/json')

    @route('/kedatech/material/delete', auth='user', type='http', methods=['POST'], csrf=False)
    def delete_material(self):
        from pudb import set_trace; set_trace()
        body = request.httprequest.json
        result = {'error': ''}

        _id = body.get('id')
        if not _id:
            result.update({'error': 'No material id to be deleted found'})

        material = request.env['kedatech.material'].browse([_id])
        material.unlink()
        
        result.update({'data': []})
        status = 200 if not result['error'] else 404

        return Response(json.dumps(result), status=status, mimetype='application/json')
