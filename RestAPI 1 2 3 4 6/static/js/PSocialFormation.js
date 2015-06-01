REG.MODELS.PSocialFormation = Backbone.Model.extend({
    urlRoot:"http://127.0.0.1:9000/api/v1/socialformation/",
         schema: {
             id: 'Number',
             Name: 'Text',
             DateReg: 'date',
             RegNumb: 'Number'

         },
         defaults:{
        id:null
    },
    idAttribute: 'id',
    validate: function (attr) {
    }
});

var PSocialFormation = Backbone.Collection.extend({
	model: REG.MODELS.PSocialFormation,
	url : 'http://127.0.0.1:9000/api/v1/socialformation/',
});

REG.COLLECTIONS.PSocialFormation = new PSocialFormation;

REG.VIEWS.ExampleListItemPSocialFormation = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>Name:</b> <%- Name %></tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePSocialFormation(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPSocialFormation(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePSocialFormation() {

    var model1 = null;
    if(document.forms.form[3].value>0) {
        model1 = new REG.MODELS.PAddress({id: document.forms.form[3].value});
        model1.fetch({wait: true});
    }

    var model2 = null;
    if(document.forms.form[4].value>0) {
        model2 = new REG.MODELS.PPerson({id: document.forms.form[4].value});
        model2.fetch({wait: true});
    }

    var model3 = null;
    if(document.forms.form[5].value>0) {
        model3 = new REG.MODELS.PTypeOfSocForm({id: document.forms.form[5].value});
        model3.fetch({wait: true});
    }

    var model4 = null;
    if(document.forms.form[6].value>0) {
        model4 = new REG.MODELS.PFormOfLeg({id: document.forms.form[6].value});
        model4.fetch({wait: true});
    }

    var pSocialFormation = new REG.MODELS.PSocialFormation(   {Name:document.forms.form[0].value,
                                            DateReg:document.forms.form[1].value,
                                            RegNumb:document.forms.form[2].value,
                                            Address:model1,
                                            Person:model2,
                                            TypeOfSocForm:model3,
                                            FormOfLeg:model4
                                            });

//    alert(JSON.stringify(pSocialFormation));

    pSocialFormation.save(null, {
          type: 'POST',
          success: function(model, response){
            console.log('success');
            updView("PSocialFormation");
          },
          error: function(){

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

function savePESocialFormation(i) {

    var model1 = null;
    if(document.forms.form[3].value>0) {
        model1 = new REG.MODELS.PAddress({id: document.forms.form[3].value});
        model1.fetch({wait: true});
    }

    var model2 = null;
    if(document.forms.form[4].value>0) {
        model2 = new REG.MODELS.PPerson({id: document.forms.form[4].value});
        model2.fetch({wait: true});
    }

    var model3 = null;
    if(document.forms.form[5].value>0) {
        model3 = new REG.MODELS.PTypeOfSocForm({id: document.forms.form[5].value});
        model3.fetch({wait: true});
    }

    var model4 = null;
    if(document.forms.form[6].value>0) {
        model4 = new REG.MODELS.PFormOfLeg({id: document.forms.form[6].value});
        model4.fetch({wait: true});
    }

    var model = REG.COLLECTIONS.PSocialFormation.findWhere({id: i});

    model.save(   {Name:document.forms.form[0].value,
                                            DateReg:document.forms.form[1].value,
                                            RegNumb:document.forms.form[2].value,
                                            Address:model1,
                                            Person:model2,
                                            TypeOfSocForm:model3,
                                            FormOfLeg:model4
                                            },
            {
            type: 'PUT',
            success: function() {
                updView("PSocialFormation");
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

function deletePSocialFormation(i) {
    var model = new REG.MODELS.PSocialFormation({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("PSocialFormation");
          }
        });
};

function editPSocialFormation(i) {
    var model = REG.COLLECTIONS.PSocialFormation.findWhere({id: i});

    document.forms.form[0].value = model.get("Name");
    document.forms.form[1].value = model.get("DateReg");
    document.forms.form[2].value = model.get("RegNumb");

    document.forms.form[3].value = model.get("Address").id;
    document.forms.form[4].value = model.get("Person").id;
    document.forms.form[5].value = model.get("TypeOfSocForm").id;
    document.forms.form[6].value = model.get("FormOfLeg").id;

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";


};

function initPSocialFormation(){
    var div = document.getElementById("form");

    var input = new Array(  document.createElement("input"),document.createElement("input"),
                            document.createElement("input"),
                             document.createElement("select"),
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

    input[2].id = "RegNumb";
    input[2].name = "RegNumb";
    input[2].maxLength = "45";
    input[2].type = "number";
    input[2].value = 0;
    ///////////////////////////////////////
    input[3].id = "Address";
    input[3].name = "Address";

    REG.COLLECTIONS.PAddress.fetch({ reset : true,
     success:function(){
        for(var i=0; i<REG.COLLECTIONS.PAddress.length; i++) {

            var opt = document.createElement("option");
            opt.value= REG.COLLECTIONS.PAddress.models[i].id;
            opt.innerHTML = REG.COLLECTIONS.PAddress.models[i].get("City") + " " + REG.COLLECTIONS.PAddress.models[i].get("Street")
             + " " + REG.COLLECTIONS.PAddress.models[i].get("House"); // whatever property it has

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


    input[5].id = "TypeOfSocForm";
    input[5].name = "TypeOfSocForm";

    REG.COLLECTIONS.PTypeOfSocForm.fetch({ reset : true,
     success:function(){
        for(var i=0; i<REG.COLLECTIONS.PTypeOfSocForm.length; i++) {

            var opt = document.createElement("option");
            opt.value= REG.COLLECTIONS.PTypeOfSocForm.models[i].id;
            opt.innerHTML = REG.COLLECTIONS.PTypeOfSocForm.models[i].get("Name"); // whatever property it has

            input[5].appendChild(opt);
        }

    }});

    input[6].id = "FormOfLeg";
    input[6].name = "FormOfLeg";

    REG.COLLECTIONS.PFormOfLeg.fetch({ reset : true,
     success:function(){
        for(var i=0; i<REG.COLLECTIONS.PFormOfLeg.length; i++) {

            var opt = document.createElement("option");
            opt.value= REG.COLLECTIONS.PFormOfLeg.models[i].id;
            opt.innerHTML = REG.COLLECTIONS.PFormOfLeg.models[i].get("Name"); // whatever property it has

            input[6].appendChild(opt);
        }

    }});
    //input[2].maxLength = "45";
    //input[2].type = "number";
    //input[2].value = 0;

    div.appendChild(input[0]); //appendChild
    div.appendChild(input[1]); //appendChild
    div.appendChild(input[2]); //appendChild
    div.appendChild(input[3]); //appendChild
    div.appendChild(input[4]); //appendChild
    div.appendChild(input[5]); //appendChild
    div.appendChild(input[6]); //appendChild
};