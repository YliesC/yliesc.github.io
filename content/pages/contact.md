Title: Contact
Order: 6
Date: 2017-07-27
Slug: contact
Author: YliesC

### Par email

Ce formulaire de contact utilisant [Formspree](https://formspree.io/) vous permet de me contacter par email. N'hésitez pas, si il y a bien un moyen de me contacter de manière sûre, c'est celui là.

<form id="contactform"  method="POST">
<div class="slideanim">
  <div class="row">
    <div class="col-sm-6 form-group">
      <input class="form-control" id="name" name="name" placeholder="Name" type="text" required>
    </div>
    <div class="col-sm-6 form-group">
      <input class="form-control" id="email" name="_replyto" placeholder="Email" type="email" required>
    </div>
  </div>
  <textarea class="form-control" id="comments" name="message" placeholder="Message" rows="5"></textarea><br>
  <div class="row">
    <div class="col-sm-12 form-group">
      <button class="btn btn-default pull-right" type="submit">Send</button>
    </div>
  </div>
</div>
<input type="text" name="_gotcha" style="display:none" />   
</form>
<script>
var contactform =  document.getElementById('contactform');
contactform.setAttribute('action', '//formspree.io/' + 'ylies' + '@' + 'thegoldenkoala' + '.' + 'com');
</script>
