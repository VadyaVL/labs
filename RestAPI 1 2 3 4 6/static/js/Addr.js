REG.MODELS.Address = Backbone.Model.extend({
    urlRoot:"/api/v1/address",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var Address = Backbone.Collection.extend({
	model: REG.MODELS.Address,
	url : '/api/v1/address',
});

REG.COLLECTIONS.Address = new Address;

REG.VIEWS.ExampleListItemAddress = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>Country:</b> <%- Country %> <b>Region:</b> <%- Region %> <b>Area:</b> <%- Area %> <b>City:</b> <%- City %></tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deleteAddress(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editAddress(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function saveAddress() {

    var address = new REG.MODELS.Address(   {Country:document.forms.form[0].value,
                                            Index:document.forms.form[1].value,
                                            Region:document.forms.form[2].value,
                                            Area:document.forms.form[3].value,
                                            City:document.forms.form[4].value,
                                            Street:document.forms.form[5].value,
                                            Home:document.forms.form[6].value});
    address.save(null, {
          success: function(model, response){
            console.log('success');
            updView("Address");
          }
        });
    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
    document.forms.form[4].value = "";
    document.forms.form[5].value = "";
    document.forms.form[6].value = "";
};

function saveEAddress(i) {
    var model = REG.COLLECTIONS.Address.findWhere({id: i});
    model.save({Country:document.forms.form[0].value,
                                            Index:document.forms.form[1].value,
                                            Region:document.forms.form[2].value,
                                            Area:document.forms.form[3].value,
                                            City:document.forms.form[4].value,
                                            Street:document.forms.form[5].value,
                                            Home:document.forms.form[6].value},
            {
            type: 'PUT',
            success: function() {
                updView("Address");
            }
        });
    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
    document.forms.form[4].value = "";
    document.forms.form[5].value = "";
    document.forms.form[6].value = "";
};

function deleteAddress(i) {
    var model = new REG.MODELS.Address({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("Address");
          }
        });
};

function editAddress(i) {
    REG.COLLECTIONS.Address.fetch({ reset : true });
    var model = REG.COLLECTIONS.Address.findWhere({id: i});

    document.forms.form[0].value = model.get("Country");
    document.forms.form[1].value = model.get("Index");
    document.forms.form[2].value = model.get("Region");
    document.forms.form[3].value = model.get("Area");
    document.forms.form[4].value = model.get("City");
    document.forms.form[5].value = model.get("Street");
    document.forms.form[6].value = model.get("Home");

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};
