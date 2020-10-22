from flask import Flask, request, jsonify, url_for, session, escape
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'khaledeCommerce'
CORS(app)

# cors=CORS(app)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ecommercekcom@gmail.com'
app.config['MAIL_PASSWORD'] = 'khaled03282016'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config ["MONGO_DBNAME"] = "eCommerce_shop"
app.config["MONGO_URI"] = "mongodb+srv://khaled:sabrina03282016@cluster0.7kuww.mongodb.net/eCommerce_shop?retryWrites=true&w=majority"
mongo = PyMongo(app)



# @app.route('/')
# def home_page():
#      return f'''
#      <h1>HELLO</h1>
#      '''

# @app.after_request
# def middleware_for_response(response):
#     # Allowing the credentials in the response.
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response


@app.route('/product/<filename>')
def get(filename):
     return mongo.send_file(filename)




def get_url(image, filename, product):
     if len(product[image])>0 :
          image_url = url_for('get',  filename = product[image])
          return "https://kcom-ecommerce-shop-api.herokuapp.com"+image_url
     else :
          a=''
     return a






@app.route('/get', methods=["GET"])
def get_products ():
     products = mongo.db.products

     output = []

     for product in products.find(): 
          
          output.append({'id': str(product['_id']),'Title': product['Title'], 'Category': product['Category'], 
          'Size':product['Size'],'Color': product['Color'],
          'Price':product['Price'],
          'image': get_url('image', product['image'], product ),
          'image_1': get_url('image_1', product['image_1'], product),
          'image_2': get_url('image_2',  product['image_2'], product),
          'image_3': get_url('image_3',  product['image_3'], product)})
          
          
    
     return  jsonify({"result": output})

def exist(image):
     if image in request.files:
          return True

def img (image):
     if image in  request.files:
          image = request.files[image]
          mongo.save_file(image.filename, image)
          return image.filename
     else: 
          a = ""
          return a


def product_output(product):
     output = {
               'id' : str(product['_id']),
               'Title': product['Title'], 
               'Category': product['Category'], 
               'Size':product['Size'],
               'Price':product['Price'],
               'Color': product['Color'],
               'image': get_url('image', product['image'], product ),
               'image_1': get_url('image_1', product['image_1'], product),
               'image_2': get_url('image_2',  product['image_2'], product),
               'image_3': get_url('image_3',  product['image_3'], product),
                }
     return output


def client_output(client):
     output = {
          'id': client['_id'],
          'last_name': client['last_name'],
          'password': client['password'],
          'name': client['name']
     }
     return output


@app.route('/test', methods=["POST"])
def test():
     products = mongo.db.products

             
     title = request.form.get('Title')
     category = request.form.get('Category')
     color = request.form.get('Color')
     Price = request.form.get('Price')
     QuantityS = request.form.get('QuantityS')
     QuantityL= request.form.get('QuantityL')
     QuantityM = request.form.get('QuantityM')
     QuantityXl = request.form.get('QuantityXl')
     QuantityXxl = request.form.get('QuantityXxl')
     kids1 = request.form.get('kids1')
     kids2 = request.form.get('kids2')
     kids3 = request.form.get('kids3')
     kids4 = request.form.get('kids4')
     kids5 = request.form.get('kids5')
     kids6 = request.form.get('kids6')
     kids7 = request.form.get('kids7')
     kids8 = request.form.get('kids8')
     kids9 = request.form.get('kids9')
     kids10 = request.form.get('kids10')
     kids11 = request.form.get('kids11')
     kids12 = request.form.get('kids12')
     kids1y = request.form.get('kids1y')
     kids2y = request.form.get('kids2y')
     kids3y = request.form.get('kids3y')
     kids4y = request.form.get('kids4y')
     kids5y = request.form.get('kids5y')
     kids6y = request.form.get('kids6y')
     kids13 = request.form.get('kids13')
     Quantity7 = request.form.get('Quantity7')
     Quantity7_5 = request.form.get('Quantity7_5')
     Quantity8 = request.form.get('Quantity8')
     Quantity8_5 = request.form.get('Quantity8_5')
     Quantity9 = request.form.get('Quantity9')
     Quantity9_5 = request.form.get('Quantity9_5')
     Quantity10 = request.form.get('Quantity10')
     quantity10_5 = request.form.get('Quantity10_5')
     Quantity11 = request.form.get('Quantity11')
     Quantity11_5 = request.form.get('Quantity11_5')
     Quantity12 = request.form.get('Quantity12')

     

     if title != "Shoes" :



          product_id = products.insert(
               {
               'Title': title, 
               'Category': category, 
               'Size':{
                    'Small':QuantityS,
                    'Large':QuantityL, 
                    'Medium': QuantityM, 
                    'X_large': QuantityXl, 
                    'XX_large': QuantityXxl},
               'Color': color, 
               'Price': Price, 
               'image': img('image'), 'image_1': img('image_1'), 
               'image_2': img('image_2'), 'image_3': img('image_3'),
               'date': datetime.utcnow(),
               })
          new_product = products.find_one({'_id': product_id})
          output = {
               'id' : str(new_product['_id']),
               'Title': new_product['Title'], 
               'Category': new_product['Category'], 
               'Size':new_product['Size'],
               'Price':new_product['Price'],
               'Color': new_product['Color'],
               'image': get_url('image', new_product['image'], new_product ),
               'image_1': get_url('image_1', new_product['image_1'], new_product),
               'image_2': get_url('image_2',  new_product['image_2'], new_product),
               'image_3': get_url('image_3',  new_product['image_3'], new_product)
                }
          
          
          
          
     if title == 'Shoes' and category == 'Kids' :
          product_id = products.insert(
               {
               'Title': title, 
               'Category': category, 
               'Size':{'kids1':kids1, 'kids2':kids2, 
                    'kids3': kids3, 'kids4': kids4, 
                    'kids5': kids5, 'kids6': kids6,
                    'kids7': kids7, 'kids8': kids8,
                    'kids9': kids9, 'kids10': kids10,
                    'kids11': kids11, 'kids12': kids12,
                    'kids13': kids13, 'kids1y': kids1y,
                    'kids2y': kids2y, 'kids3y': kids3y,
                    'kids4y': kids4y, 'kids5y': kids5y,
                    'kids6y': kids6y},
               'Color': color, 
               'Price': Price, 
               'image': img('image'), 'image_1': img('image_1'), 
               'image_2': img('image_2'), 'image_3': img('image_3'),
               'date': datetime.utcnow()
               })
          new_product = products.find_one({'_id': product_id})
          output = {
               'id' : str(new_product['_id']),
               'Title': new_product['Title'], 
               'Category': new_product['Category'], 
               'Size':new_product['Size'],
               'Color': new_product['Color'],
               'Price':new_product['Price'],
               'image': get_url('image', new_product['image'], new_product ),
               'image_1': get_url('image_1', new_product['image_1'], new_product),
               'image_2': get_url('image_2',  new_product['image_2'], new_product),
               'image_3': get_url('image_3',  new_product['image_3'], new_product)
                }
          
     if category != "Kids" and title == "Shoes" :

           product_id = products.insert(
               {
               'Title': title, 
               'Category': category, 
               'Size':{'size_7':Quantity7, 'size_7_5': Quantity7_5, 
                    'size_8': Quantity8, 'size_8_5': Quantity8_5, 
                    'size_9': Quantity9, 'size_9_5': Quantity9_5,
                    'size_10': Quantity10, 'size_10_5': quantity10_5,
                    'size_11': Quantity11, 'size_11_5': Quantity11_5,
                    'size_12': Quantity12},
               'Color': color, 
               'Price': Price, 
               'image': img('image'), 'image_1': img('image_1'), 
               'image_2': img('image_2'), 'image_3': img('image_3'),
               'date': datetime.utcnow()
               })
                
           new_product = products.find_one({'_id': product_id})
           output = {
               'id' : str(new_product['_id']),
               'Title': new_product['Title'], 
               'Category': new_product['Category'], 
               'Size':new_product['Size'],
               'Color': new_product['Color'],
               'Price':new_product['Price'],
               'image': get_url('image', new_product['image'], new_product ),
               'image_1': get_url('image_1', new_product['image_1'], new_product),
               'image_2': get_url('image_2',  new_product['image_2'], new_product),
               'image_3': get_url('image_3',  new_product['image_3'], new_product)
                }
               
     
     
     return jsonify({'result': output})



@app.route('/get/<Id>', methods=["GET"])
def get_product (Id):
    
     products = mongo.db.products

     
         
     output_id = products.find_one({'_id': ObjectId(Id)})

     output = {
               'id': str(output_id['_id']),
               'Title': output_id['Title'], 
               'Category': output_id['Category'], 
               'Size':output_id['Size'],
               'Color': output_id['Color'],
               'Price': output_id['Price'],
               'image': get_url('image', output_id['image'], output_id ),
               'image_1': get_url('image_1', output_id['image_1'], output_id),
               'image_2': get_url('image_2', output_id['image_2'], output_id),
               'image_3': get_url('image_3', output_id['image_3'], output_id)
               }

    
     return   jsonify({'result': output})

@app.route('/get/<Title>/<Category>', methods=["GET"])
def get_product_by_title_category (Title, Category):
    
     products = mongo.db.products
     list_products=[]

     
     
     for product in products.find({'Title':Title, 'Category': Category}):

           list_products.append( {
                    'id': str(product['_id']),
                    'Title': product['Title'], 
                    'Category': product['Category'], 
                    'Size':product['Size'],
                    'Price': product['Price'],
                    'Color': product['Color'], 
                    'image': get_url('image', product['image'], product ),
                    'image_1': get_url('image_1', product['image_1'], product),
                    'image_2': get_url('image_2', product['image_2'], product),
                    'image_3': get_url('image_3', product['image_3'], product)
                     })

    
     return   jsonify({'result': list_products})



@app.route('/get/product/<Category>', methods=["GET"])
def get_product_by_title (Category):
    
     products = mongo.db.products
     list_products=[]

     
     
     for product in products.find({'Category':Category}):

           list_products.append( product_output(product))

    
     return   jsonify({'result': list_products})


@app.route('/delete/<Id>', methods=["Delete"])
def delete_product (Id):
    
     products = mongo.db.products
         
     output= products.remove({'_id': ObjectId(Id)})


    
     return   jsonify({'result': output})


def img_update(Id, products, image_0):
     product= products.find_one({'_id':ObjectId(Id)})
     if len(product[image_0])>0:
          img_existe = product[image_0]
          return img_existe
     else : 
          img_existe = img(image_0)
          return img_existe


@app.route('/update_product/<Id>', methods=["PATCH"])
def update(Id):
     products = mongo.db.products

    
             
     title = request.form.get('Title')
     category = request.form.get('Category')
     color = request.form.get('Color')
     Price = request.form.get('Price')
     QuantityS = request.form.get('QuantityS')
     QuantityL= request.form.get('QuantityL')
     QuantityM = request.form.get('QuantityM')
     QuantityXl = request.form.get('QuantityXl')
     QuantityXxl = request.form.get('QuantityXxl')
     kids1 = request.form.get('kids1')
     kids2 = request.form.get('kids2')
     kids3 = request.form.get('kids3')
     kids4 = request.form.get('kids4')
     kids5 = request.form.get('kids5')
     kids6 = request.form.get('kids6')
     kids7 = request.form.get('kids7')
     kids8 = request.form.get('kids8')
     kids9 = request.form.get('kids9')
     kids10 = request.form.get('kids10')
     kids11 = request.form.get('kids11')
     kids12 = request.form.get('kids12')
     kids1y = request.form.get('kids1y')
     kids2y = request.form.get('kids2y')
     kids3y = request.form.get('kids3y')
     kids4y = request.form.get('kids4y')
     kids5y = request.form.get('kids5y')
     kids6y = request.form.get('kids6y')
     kids13 = request.form.get('kids13')
     Quantity7 = request.form.get('Quantity7')
     Quantity7_5 = request.form.get('Quantity7_5')
     Quantity8 = request.form.get('Quantity8')
     Quantity8_5 = request.form.get('Quantity8_5')
     Quantity9 = request.form.get('Quantity9')
     Quantity9_5 = request.form.get('Quantity9_5')
     Quantity10 = request.form.get('Quantity10')
     quantity10_5 = request.form.get('Quantity10_5')
     Quantity11 = request.form.get('Quantity11')
     Quantity11_5 = request.form.get('Quantity11_5')
     Quantity12 = request.form.get('Quantity12')
     

     

     if title != "Shoes" :



          products.update({'_id': ObjectId(Id)},
               { '$set':
               {'Title': title,
               'Category': category,  
               'Size.Small':QuantityS, 
               'Size.Large':QuantityL, 
               'Size.Medium': QuantityM, 
               'Size.X_large': QuantityXl, 
               'Size.XX_large': QuantityXxl,
               'Price': Price,
               'Color': color,
               'image': img_update(Id, products, 'image'),
               'image_1': img_update(Id, products, 'image_1'),
               'image_2': img_update(Id, products, 'image_2'),
               'image_3': img_update(Id, products, 'image_3')}})

               

          new_product = products.find_one({'_id': ObjectId(Id)})
          output = {
               'id' : str(new_product['_id']),
               'Title': new_product['Title'], 
               'Category': new_product['Category'], 
               'Size':new_product['Size'],
               'Color': new_product['Color'],
               'image': get_url('image', new_product['image'], new_product ),
               'image_1': get_url('image_1', new_product['image_1'], new_product),
               'image_2': get_url('image_2',  new_product['image_2'], new_product),
               'image_3': get_url('image_3',  new_product['image_3'], new_product)
                }
          
          
          
          
     if title == 'Shoes' and category == 'Kids' :
          products.update({'_id': ObjectId(Id)},
               { '$set':
               {'Title': title, 
               'Category': category, 
               'Size.kids1':kids1, 'Size.kids2':kids2, 
               'Size.kids3': kids3, 'Size.kids4': kids4, 
               'Size.kids5': kids5, 'Size.kids6': kids6,
               'Size.kids7': kids7, 'Size.kids8': kids8,
               'Size.kids9': kids9, 'Size.kids10': kids10,
               'Size.kids11': kids11, 'Size.kids12': kids12,
               'Size.kids13': kids13, 'Size.kids1y': kids1y,
               'Size.kids2y': kids2y, 'Size.kids3y': kids3y,
               'Size.kids4y': kids4y, 'Size.kids5y': kids5y,
               'Size.kids6y': kids6y,
               'Color': color, 
               'Price': Price, 
               'image': img_update(Id, products, 'image'),
               'image_1': img_update(Id, products, 'image_1'),
               'image_2': img_update(Id, products, 'image_2'),
               'image_3': img_update(Id, products, 'image_3')}})

          new_product = products.find_one({'_id': ObjectId(Id)})
          output = {
               'id' : str(new_product['_id']),
               'Title': new_product['Title'], 
               'Category': new_product['Category'], 
               'Size':new_product['Size'],
               'Color': new_product['Color'],
               'Price':new_product['Price'],
               'image': get_url('image', new_product['image'], new_product ),
               'image_1': get_url('image_1', new_product['image_1'], new_product),
               'image_2': get_url('image_2',  new_product['image_2'], new_product),
               'image_3': get_url('image_3',  new_product['image_3'], new_product)
                }
          
     if category != "Kids" and title == "Shoes" :

          products.update({'_id': ObjectId(Id)},
               { '$set':
               {'Title': title, 
               'Category': category, 
               'Size.size_7':Quantity7, 'Size.size_7_5': Quantity7_5, 
               'Size.size_8': Quantity8, 'Size.size_8_5': Quantity8_5, 
               'Size.size_9': Quantity9, 'Size.size_9_5': Quantity9_5,
               'Size.size_10': Quantity10, 'Size.size_10_5': quantity10_5,
               'Size.size_11': Quantity11, 'Size.size_11_5': Quantity11_5,
               'Size.size_12': Quantity12,
               'Color': color, 
               'Price': Price, 
               'image_1': img_update(Id, products, 'image_1'),
               'image_2': img_update(Id, products, 'image_2'),
               'image_3': img_update(Id, products, 'image_3')}})
                
          new_product = products.find_one({'_id': ObjectId(Id)})
          output = {
                    'id' : str(new_product['_id']),
                    'Title': new_product['Title'], 
                    'Category': new_product['Category'], 
                    'Size':new_product['Size'],
                    'Color': new_product['Color'],
                    'Price':new_product['Price'],
                    'image': get_url('image', new_product['image'], new_product ),
                    'image_1': get_url('image_1', new_product['image_1'], new_product),
                    'image_2': get_url('image_2',  new_product['image_2'], new_product),
                    'image_3': get_url('image_3',  new_product['image_3'], new_product)
                    }
                    
     
     
     return jsonify({'result': output})


def image_name(image_url):
  image=image_url.rsplit('/')
  return image[-1]


@app.route ('/delete_image/<Id>/<image_order>', methods = ["Patch"])
def delete_iamge(Id, image_order):

     products =  mongo.db.products

     products.update({'_id': ObjectId(Id)}, {"$set":
     {
          image_order :''
     }})
     new_product = products.find_one({'_id': ObjectId(Id)})
     output = {
                    'id' : str(new_product['_id']),
                    'Title': new_product['Title'], 
                    'Category': new_product['Category'], 
                    'Size':new_product['Size'],
                    'Color': new_product['Color'],
                    'Price':new_product['Price'],
                    'image': get_url('image', new_product['image'], new_product ),
                    'image_1': get_url('image_1', new_product['image_1'], new_product),
                    'image_2': get_url('image_2',  new_product['image_2'], new_product),
                    'image_3': get_url('image_3',  new_product['image_3'], new_product)
                    }
    
     return jsonify({'result': output})

@app.route('/management/admin-auth/session', methods=["Post"])
def logged_in():
     admins = mongo.db.admins
     username = request.json['user_name']
     password = request.json['password']
     admin_id = admins.find_one({'user_name': username, 'Password': password})
     if admin_id :
          session['status']= 'created'
          output= session['status']
     else:
           output='not found'         
               
     return jsonify({'result': output})


@app.route('/management/get_login_status/', methods=["GET"])
def get_login_status():
      
      if 'status'  in session:
            status = True
      else :
            status = False
     
      return jsonify({'result': status})


@app.route('/management/admin-auth/logout/', methods=["DELETE"])
def delete_admin_session():
      
     session.pop('status', None)


     if 'status'  in session:
            status = True
     else :
            status = False
     
     return jsonify({'result': status})



@app.route('/client/auth/session', methods=["Post"])
def client_logged_in():
     members = mongo.db.members
     email = request.json['email']
     password = request.json['password']
     member_id = members.find_one({'_id': email.lower(), 'password': password})
     if member_id :
          session['client_status']= {'status': 'created', 'email': email}
          output= session['client_status']
     else:
           output='not found'         
               
     return jsonify({'result': output})


@app.route('/client/get_login_status/', methods=["GET"])
def client_get_login_status():
      
      if 'client_status'  in session:
            status = {'status':True, 'email': session['client_status']['email']}
      else :
            status = {'status':False, 'email': ''}
     
      return jsonify({'result': status})


@app.route('/client/auth/logout/', methods=["DELETE"])
def client_delete_auth_session():
      
     session.pop('client_status', None)


     if 'client_status'  in session:
            status = True
     else :
            status = False
     
     return jsonify({'result': status})


@app.route('/product/last-release', methods=["GET"])
def get_last_release():
     products = mongo.db.products
     output = []
     for product in products.find({"Category": "Men"}).sort([("date", -1)]).limit(3):
          output.append (product_output(product))
     for prod in products.find({"Category": "Women"}).sort([("date", -1)]).limit(3):
          output.append (product_output(prod))
     for pro in products.find({"Category": "Kids"}).sort([("date", -1)]).limit(3):
          output.append (product_output(pro))
     
     return jsonify({"result": output})



@app.route('/client/signup', methods = ["POST"])
def signup_client():
     members= mongo.db.members
     name = request.form.get('name')
     password = request.form.get('password')
     last_name = request.form.get('last_name')
     email = request.form.get('email')
     
     member_id = members.insert({
          '_id': email.lower(),
          'password': password,
          'last_name': last_name,
          'name': name,
          'cart_shop':{'cart':[], 'subtotal':0},
          'orders':[]
          })
     member = members.find_one({'_id': member_id})
     output = client_output(member)
     msg = Message('Welcom To Kcom.com', sender = 'ecommercekcom@gmail.com', recipients = [member['_id']])
     msg.body = f'''{name} {last_name}, Thank You for your subscription.'''
     mail.send(msg)

     return jsonify({'result': output})




@app.route('/shop/cart', methods = ["POST"])
def cart_session():
     product_id = request.json['id']
     size = request.json['size']
     quantity = request.json['quantity']
     price = request.json['price']

     if 'cart_shop' in session:
          
          session['cart_shop'] = {'cart': session['cart_shop']['cart'] + [{'product_id': product_id,
                         'size': size,
                         'quantity': quantity,
                         'price': price}], 'total': session['cart_shop']['total'] + price}
          output= session['cart_shop']
     else: 
          session['cart_shop'] = {'cart':[{'product_id': product_id,
                         'size': size,
                         'quantity': quantity,
                         'price': price}], 'total':price}
          output = session['cart_shop']
     

     return jsonify({'result': output})


@app.route('/shop/cart/delete_guest_cart_shop/<product_id>', methods= ['DELETE'])
def delete_cart_product(product_id):
     if ('cart_shop' in session) and (len(session['cart_shop']['cart'])>1):
          for product in session['cart_shop']['cart']:
               
                    if product['product_id'] == product_id:
                         session['cart_shop']['cart'].remove(product)
                         session['cart_shop']['total']= session['cart_shop']['total'] - product['price']
                         session['cart_shop']= session['cart_shop']
                         return jsonify({'result': session['cart_shop']})
     else:
          
          session.pop('cart_shop', None)
          if 'cart_shop' in session:
               output = False
          else:
               output = True

          return jsonify({'result': output}) 



     



@app.route('/shop/cart/get_guest_products', methods = ['GET'])
def get_guests_products():
     if 'cart_shop' in session:
          output = session['cart_shop']
     else:
          output = 'not found'

     
     return jsonify({'result': output})



@app.route('/shop/cart/members_cart_shop', methods = ['PATCH'])
def members_cart():
     members = mongo.db.members
     member_id = request.json['email']
     product_id = request.json['id']
     size = request.json['size']
     quantity = request.json['quantity']
     price = request.json['price']
     

     member_updated = members.find_one({'_id': member_id})
     new_subtotal = member_updated['cart_shop']['subtotal'] + price

     members.update({'_id': member_id}, {'$set': {'cart_shop.subtotal': new_subtotal},'$push':{
          'cart_shop.cart':{'product_id': product_id,
                        'size':size,
                        'quantity':quantity,
                        'price': price}}
     }) 

     
          
     

     output = {'id': member_updated['_id'],
               'name': member_updated['name'],
               'cart_shop': member_updated['cart_shop'], 
     }


     return jsonify({'result': output})


@app.route('/shop/cart/get_members_products/<email>', methods = ['GET'])
def get_members_products(email):
     members = mongo.db.members

     
     member_cart = members.find_one({'_id': email})
     cart_shop = member_cart['cart_shop']
     output = cart_shop

          
     return jsonify({'result': output})



@app.route('/shop/cart/remove_members_cart_shop/<email>/<product_id>', methods=['PATCH'])
def remove_cart_item(email,product_id):
     members= mongo.db.members

     member_updated = members.find_one({'_id': email})
     

     for item in member_updated['cart_shop']['cart']:
          if item['product_id']==product_id:
          
               result = members.update_one({'_id':email},{'$set':{'cart_shop.subtotal': member_updated['cart_shop']['subtotal']-item['price']},'$pull':{'cart_shop.cart':{'product_id':product_id}}}, False)

     return jsonify({'result':result.modified_count})  



@app.route('/shop/shipment/shipment_informaion', methods=['PATCH'])
def post_orders():
     orders = mongo.db.orders
     # guest_name = request.json['guest_name']
     # guest_last_name = request.json['guest_last_name']
     members = mongo.db.members

     logged_in_status = request.json['logged_in_status']
     email = request.json['email']
     guest_email = request.json['guest_email']
     list_of_orders = request.json['list_of_orders']
     total = request.json['total']
     shipment_adress = request.json['shipment_adress']
     payement_information = request.json['payement_information']
     products = mongo.db.products
     total_items=0
     for item in list_of_orders:
          total_items += int(item['quantity'])

     new_order_id = orders.insert({
          'email': guest_email,
          'list_of_orders': list_of_orders,
          'shipping_adress': shipment_adress,
          'payement_information': payement_information,
          'total': total,
          'date': datetime.utcnow(),
          'total_item':total_items
     })

     new_order = orders.find_one({'_id':new_order_id})

     if logged_in_status == 'LOGGED_IN':
          members.update({'_id': email}, {'$push':{
          'orders':{'_id': new_order['_id'],
                    'list_of_orders': list_of_orders,
                    'total': total,
                    'shipping_adress':shipment_adress,
                    'payement_information': payement_information,
                    'date': datetime.utcnow(),
                    'total_item': total_items}}})

     for order in new_order['list_of_orders']:
          size = order['size']
          product_to_update = products.find_one({'_id': ObjectId(order['product_id'])})
          size_to_update = product_to_update['Size'][size]
          products.update_one({'_id': ObjectId(order['product_id'])}, {
               '$set':{
                   f'Size.{size}': int(size_to_update) - int(order['quantity'])
               }
          })
     msg = Message(f'Thank You for Your Order({new_order_id})', sender = 'ecommercekcom@gmail.com', recipients = [guest_email])
     msg.body = f'''
     Shipping to: {new_order["shipping_adress"]["name"]} {new_order["shipping_adress"]["last_name"]}
     {new_order["shipping_adress"]["street"]},{new_order["shipping_adress"]["city"]},{new_order["shipping_adress"]["state"]},{new_order["shipping_adress"]["zipcode"]}
     
     Thank's, {new_order["shipping_adress"]["name"]}!
     We're On It.
     
     Order Number: {new_order_id}
     Order Date: {new_order["date"]}
     '''
     mail.send(msg)

     
     output = {
          "id":str(new_order['_id']),
          "guest_name": new_order['shipping_adress']['name'],
          "guest_last_name": new_order['shipping_adress']['last_name'],
          "guest_email": new_order['email'],
          "list_of_orders": new_order['list_of_orders'],
          "shipment_adress": new_order['shipping_adress'],
          "payement_information": new_order['payement_information'],
          "total": new_order['total'],
          "date":new_order['date'],
          "total_item": new_order['total_item']
     }

     return jsonify({'result': output})




@app.route("/shop/delete/cart_session", methods=["DELETE"])
def delete_cart_session():
     
     session.pop('cart_shop', None)
     if 'cart_shop' in session:
               output = False
     else:
               output = True

     return jsonify({'result': output})


@app.route("/shop/delete/member_cart_session/<email>", methods=["PATCH"])
def delete_cart_members(email):
     
     members= mongo.db.members
     
     members.update({'_id': email},{'$set':{
          'cart_shop.subtotal':0,
          'cart_shop.cart':[]
     }})
     member_updated = members.find_one({'_id': email})
     if(len(member_updated['cart_shop']['cart'])==0):
          output = True
     else:
          output = False  


     return jsonify({'result': output})


@app.route('/order/order-details/<order_id>', methods=['GET'])
def get_order(order_id):
     orders = mongo.db.orders
     order_confirmed = orders.find_one({'_id': ObjectId(order_id)})
     output = {
          "id":str(order_confirmed['_id']),
          "guest_name": order_confirmed['shipping_adress']['name'],
          "guest_last_name": order_confirmed['shipping_adress']['last_name'],
          "guest_email": order_confirmed['email'],
          "list_of_orders": order_confirmed['list_of_orders'],
          "shipment_adress": order_confirmed['shipping_adress'],
          "card_number": f'''********{order_confirmed['payement_information']['card_number'][-4:]}''',
          "total": order_confirmed['total'],
          "date":order_confirmed['date'],
          "total_item": order_confirmed['total_item']
     }

     return jsonify({'result': output})

@app.route("/orders/get_orders", methods=['GET'])
def get_list_orders():
     orders= mongo.db.orders
     list_of_orders = []


     for order in orders.find():
          list_of_orders.append({'order_id': str(order['_id']),
          'guest_name':f'''{order['shipping_adress']['name']} {order['shipping_adress']['last_name']}''',
          'total': order['total'],
          'shipping_address': f'''{order['shipping_adress']['city']}, {order['shipping_adress']['state']}, {order['shipping_adress']['zipcode']}''',
          'date':order['date']
          })

     return jsonify({'result': list_of_orders})



@app.route("/orders/members/history/<Id>", methods=['GET'])
def members_history_orders(Id):
     members= mongo.db.members
     list_of_orders = []


     member = members.find_one({'_id': Id})
     for order in member['orders']:
          list_of_orders.append({
          'order_id': str(order['_id']),
          'guest_name':f'''{order['shipping_adress']['name']} {order['shipping_adress']['last_name']}''',
          'total': order['total'],
          'shipping_address': f'''{order['shipping_adress']['city']}, {order['shipping_adress']['state']}, {order['shipping_adress']['zipcode']}''',
          'date':order['date']
          })
         

     return jsonify({'result': list_of_orders})



     


if __name__ == '__main__':
    app.run(debug=True)