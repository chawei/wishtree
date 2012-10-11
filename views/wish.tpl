<!doctype html>
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!-- Consider adding a manifest.appcache: h5bp.com/d/Offline -->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8">

  <!-- Use the .htaccess and remove these lines to avoid edge case issues.
       More info: h5bp.com/i/378 -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>{{result['title']}}</title>
  <meta name="description" content="">
  <!-- Mobile viewport optimized: h5bp.com/viewport -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=no">
  <!-- Place favicon.ico and apple-touch-icon.png in the root directory: mathiasbynens.be/notes/touch-icons -->
  <link rel="stylesheet" type="text/css" href="/css/app.css">
  <link rel="stylesheet" type="text/css" href="/css/mobile.css">
  <!-- More ideas for your head here: h5bp.com/d/head-Tips -->
  
  <!-- Want to try a different theme?
  	   If not using LESS compiler: Uncomment below
       and change to name of desired theme. (See docs) 	-->
  <!--link type="text/css" rel="stylesheet" href="/extras/css/amelia.css" /-->

  <!-- All JavaScript at the bottom, except this Modernizr build.
       Modernizr enables HTML5 elements & feature detects for optimal performance.
       Create your own custom Modernizr build: www.modernizr.com/download/ -->
  <script src="/static/js/modernizr-2.5.3.min.js"></script>
  
  <style>@import url("//fonts.googleapis.com/css?family=Nunito:300normal,400normal,700normal&subset=latin&directory&text=+%2C-.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz&directory");</style>
  
  <script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-35388799-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

  </script>
</head>
<body>
  <!-- Prompt IE 6 users to install Chrome Frame. Remove this if you support IE 6.
       chromium.org/developers/how-tos/chrome-frame-getting-started -->
  <!--[if lt IE 7]>
    <link href="/css/bootstrap.ie6.css" rel="stylesheet">
  	<p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p>
  <![endif]-->

  <div class="navbar">
    <div class="navbar-inner">
      <div class="container">
        <!-- Be sure to leave the brand out there if you want it shown -->
        <a class="brand" href="/">Wishtree</a>
      </div>
    </div>
  </div>

  <div id="main">
    <div class="container">      
      <header id="overview" class="cf">
        <div class="inner">
          <div class="desc">
            <div class="image">
              <img src="{{result['user']['avatar']['url']}}">
            </div>
            <div class='wishtitle'>
              <h3><span class="name">{{result['user']['nickname']}}</span><span class="action"> wished : </span>{{result['title']}}</h3>
            </div>
          </div>
          <div class="transparent-bg"></div>
          
          <div id="marketing_section">
            <a class="app-store-badge" href="http://itunes.apple.com/us/app/wishtree-record-every-memorized/id554099143?ls=1&mt=8"></a>
            <div class="fb-like" data-send="false" data-layout="button_count" data-width="100" data-show-faces="false" data-font="lucida grande"></div>
          </div>
        </div>
      </header>
      
      <div class="storyline">
        <div class="story cf">
          <div class="image">
            <img class ="icon" src="{{result['treeState']['photoFile']['url']}}">
            <img class ="uploaded-img" src="{{result['image']['url']}}">
          </div>
          
          <h4 class="title">{{!result['description']}}</h4>
        </div>
        
        %for photo in result['photoList'] :
        <div class="timestamp">{{photo['delta']}}</div>
        
        <div class="story cf">
          <div class="image">
            <img class ="icon" src="{{photo['treeState']['photoFile']['url']}}">
            <img class ="uploaded-img" src="{{photo['image']['url']}}">
          </div>
          
          <h4 class="title">{{!photo['description']}}</h4>
        </div>
        %end
        <div class="timestamp">{{result['delta']}}</div>
      </div>
      
    </div>
  </div>
  
  <!-- JavaScript at the bottom for fast page loading -->
  
  <!-- facebook like button -->
  <div id="fb-root"></div>
  <script>(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=438745949501972";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));</script>

  <!-- Grab Google CDN's jQuery, with a protocol relative URL; fall back to local if offline -->
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  <script>window.jQuery || document.write('<script src="/static/js/jquery-1.7.1.min.js"><\/script>')</script>
  <!-- scripts concatenated and minified via ant build script-->
  <script src="/static/js/prettify/prettify.js"></script>
  
  <!-- end scripts-->

  <!-- Asynchronous Google Analytics snippet. Change UA-XXXXX-X to be your site's ID.
       mathiasbynens.be/notes/async-analytics-snippet -->

  <script type="text/javascript">
  // Use the modernizr.load() function to run polyfills for older browsers.
    Modernizr.load({
    });
  </script>

  <!-- A little ie7- magic -->
  <script type="text/javascript"> $(function(){if($.browser.msie&&parseInt($.browser.version,10)===6){$('.row div[class^="span"]:last-child').addClass("last-child");$('[class="span"]').addClass("margin-left-20");$(':button[class="btn"], :reset[class="btn"], :submit[class="btn"], input[type="button"]').addClass("button-reset");$(":checkbox").addClass("input-checkbox");$('[class^="icon-"], [class=" icon-"]').addClass("icon-sprite");$(".pagination li:first-child a").addClass("pagination-first-child")}}) </script>
</body>
</html>