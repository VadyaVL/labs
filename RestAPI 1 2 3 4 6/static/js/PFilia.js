REG.MODELS.PFilia = Backbone.Model.extend({
    urlRoot:"http://127.0.0.1:9000/api/v1/filia/",
         schema: {
             id: 'Number',
             Name: 'Text',
             DateReg: 'date'
         },
         defaults:{
        id:null
    },
    idAttribute: 'id',
    validate: function (attr) {
    }
});

var PFilia = Backbone.Collection.extend({
	model: REG.MODELS.PFilia,
	url : 'http://127.0.0.1:9000/api/v1/filia/',
});

REG.COLLECTIONS.PFilia = new PFilia;

REG.VIEWS.ExampleListItemPFilia = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>Name:</b> <%- Name %></tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePFilia(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPFilia(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePFilia() {

    var model1 = null;
    if(document.forms.form[2].value>0) {
        model1 = new REG.MODELS.PAddress({id: document.forms.form[2].value});
        model1.fetch({wait: true});
    }

    var model2 = null;
    if(document.forms.form[3].value>0) {
        model2 = new REG.MODELS.PPerson({id: document.forms.form[3].value});
        model2.fetch({wait: true});
    }

    var model3 = null;
    if(document.forms.form[4].value>0) {
        model3 = new REG.MODELS.PTypeOfSocForm({id: document.forms.form[4].value});
        model3.fetch({wait: true});
    }

    var pFilia = new REG.MODELS.PFilia(   {Name:document.forms.form[0].value,
                                            DateReg:document.forms.form[1].value,
                                            SocialFormation:model1,
                                            Address:model2,
                                            Person:model3,
                                            });

//    alert(JSON.stringify(pSocialFormation));

    pFilia.save(null, {
          type: 'POST',
          success: function(model, response){
            console.log('success');
            updView("PFilia");
          },
          error: function(){

          }
        });

    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
    document.forms.form[4].value = "";
};

function savePEFilia(i) {

    var model1 = null;
    if(document.forms.form[2].value>0) {
        model1 = new REG.MODELS.PAddress({id: document.forms.form[2].value});
        model1.fetch({wait: true});
    }

    var model2 = null;
    if(document.forms.form[3].value>0) {
        model2 = new REG.MODELS.PPerson({id: document.forms.form[3].value});
        model2.fetch({wait: true});
    }

    var model3 = null;
    if(document.forms.form[4].value>0) {
        model3 = new REG.MODELS.PTypeOfSocForm({id: document.forms.form[4].value});
        model3.fetch({wait: true});
    }

    var model = REG.COLLECTIONS.PFilia.findWhere({id: i});

    model.save(   {Name:document.forms.form[0].value,
                                            DateReg:document.forms.form[1].value,
                                            SocialFormation:model1,
                                            Address:model2,
                                            Person:model3,
                                            },
            {
            type: 'PUT',
            success: function() {
                updView("PFilia");
            }
        });

    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
    document.forms.form[4].value = "";
};

function deletePFilia(i) {
    var model = new REG.MODELS.PFilia({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("PFilia");
          }
        });
};

function editPFilia(i) {
    var model = REG.COLLECTIONS.PFilia.findWhere({id: i});

    document.forms.form[0].value = model.get("Name");
    document.forms.form[1].value = model.get("DateReg");

    document.forms.form[2].value = model.get("SocialFormation").id;
    document.forms.form[3].value = model.get("Address").id;
    document.forms.form[4].value = model.get("Person").id;

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";


};

function initPFilia(){
    var div = document.getElementById("form");

    var input = new Array(  document.createElement("input"),document.createElement("input"),
                             document.createElement("select"),
                             document.createElement("select"),
                             document.createElement("select"));

    input[0].id = "Name";
    input[0].name = "Name";
    input[0].maxLength = "45";
    input[0].type = "text";
    input[0].value = "Назва";

    input[1].id = "DateReg";
    input[1].name = "DateReg";
    input[1].type = "Date";
    //input[1].value = "Вулиця";

    input[2].id = "SocialFormation";
    input[2].name = "SocialFormation";

    REG.COLLECTIONS.PSocialFormation.fetch({ reset : true,
     success:function(){
        for(var i=0; i<REG.COLLECTIONS.PSocialFormation.length; i++) {

            var opt = document.createElement("option");
            opt.value= REG.COLLECTIONS.PSocialFormation.models[i].id;
            opt.innerHTML = REG.COLLECTIONS.PSocialFormation.models[i].get("Name") + " " + REG.COLLECTIONS.PSocialFormation.models[i].get("RegNumb");

            input[2].appendChild(opt);
        }

    }});


    input[3].id = "Address";
    input[3].name = "Address";

    REG.COLLECTIONS.PAddress.fetch({ reset : true,
     success:function(){
        for(var i=0; i<REG.COLLECTIONS.PAddress.length; i++) {

            var opt = document.createElement("option");
            opt.value= REG.COLLECTIONS.PAddress.models[i].id;
            opt.innerHTML = REG.COLLECTIONS.PAddress.models[i].get("City") + " " + REG.COLLECTIONS.PAddress.models[i].get("Street")
             + " " + REG.COLLECTIONS.PAddress.models[i].get("House");

            input[3].appendChild(opt);
        }

    }});


    input[4].id = "Person";
    input[4].name = "Person";

     REG.COLLECTIONS.PPerson.fetch({ reset : true,
     success:function(){
        for(var i=0; i<REG.COLLECTIONS.PPerson.length; i++) {

            var opt = document.createElement("option");
            opt.value= REG.COLLECTIONS.PPerson.models[i].id;
            opt.innerHTML = REG.COLLECTIONS.PPerson.models[i].get("Name") + " " + REG.COLLECTIONS.PPerson.models[i].get("Surname"); // whatever property it has

            input[4].appendChild(opt);
        }

    }});


    div.appendChild(input[0]); //appendChild
    div.appendChild(input[1]); //appendChild
    div.appendChild(input[2]); //appendChild
    div.appendChild(input[3]); //appendChild
    div.appendChild(input[4]); //appendChild
};