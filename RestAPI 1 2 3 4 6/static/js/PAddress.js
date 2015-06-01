REG.MODELS.PAddress = Backbone.Model.extend({
    urlRoot:"http://127.0.0.1:9000/api/v1/address/",
         schema: {
             id: 'Number',
             City: 'Text',
             Street: 'Text',
             House: 'Text',
             Phone: 'Text'
         },
         defaults:{
        id:null
    },
    idAttribute: 'id',
    validate: function (attr) {
    }
});

var PAddress = Backbone.Collection.extend({
	model: REG.MODELS.PAddress,
	url : 'http://127.0.0.1:9000/api/v1/address/',
});

REG.COLLECTIONS.PAddress = new PAddress;

REG.VIEWS.ExampleListItemPAddress = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>City:</b> <%- City %> <b>Street:</b> <%- Street %> <b>House:</b> <%- House %> <b>Phone:</b> <%- Phone %> </tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePAddress(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPAddress(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePAddress() {

    var address = new REG.MODELS.PAddress(   {City:document.forms.form[0].value,
                                            Street:document.forms.form[1].value,
                                            House:document.forms.form[2].value,
                                            Phone:document.forms.form[3].value});
    address.save(null, {
          type: 'POST',
          success: function(model, response){
            console.log('success');
            updView("PAddress");
          }
        });
    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
};

function savePEAddress(i) {
    var model = REG.COLLECTIONS.PAddress.findWhere({id: i});
    model.save({City:document.forms.form[0].value,
                                            Street:document.forms.form[1].value,
                                            House:document.forms.form[2].value,
                                            Phone:document.forms.form[3].value},
            {
            type: 'PUT',
            success: function() {
                updView("PAddress");
            }
        });
    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
};

function deletePAddress(i) {
    var model = new REG.MODELS.PAddress({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("PAddress");
          }
        });
};

function editPAddress(i) {
    var model = REG.COLLECTIONS.PAddress.findWhere({id: i});

    document.forms.form[0].value = model.get("City");
    document.forms.form[1].value = model.get("Street");
    document.forms.form[2].value = model.get("House");
    document.forms.form[3].value = model.get("Phone");

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};

function initPAddressFrom(){
    var div = document.getElementById("form");

    var input = new Array(  document.createElement("input"),document.createElement("input"),
                            document.createElement("input"),document.createElement("input") );
    input[0].id = "City";
    input[0].name = "City";
    input[0].maxLength = "45";
    input[0].type = "text";
    input[0].value = "Місто";

    input[1].id = "Street";
    input[1].name = "Street";
    input[1].maxLength = "45";
    input[1].type = "text";
    input[1].value = "Вулиця";

    input[2].id = "House";
    input[2].name = "House";
    input[2].maxLength = "45";
    input[2].type = "text";
    input[2].value = "Будинок";

    input[3].id = "Phone";
    input[3].name = "Phone";
    input[3].maxLength = "45";
    input[3].type = "text";
    input[3].value = "Телефон";

    div.appendChild(input[0]); //appendChild
    div.appendChild(input[1]); //appendChild
    div.appendChild(input[2]); //appendChild
    div.appendChild(input[3]); //appendChild
};