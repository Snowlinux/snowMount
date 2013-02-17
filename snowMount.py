  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>snowMount/snowMount.py at d4c918ce836f98b6b80597f93e261b79d1d06fc3 · Snowlinux/snowMount · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="06QSqWxh+3/Xi9mJOQFpfZWgQ+iy9UOX4apH4Jhz3wg=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-053ef9e31e0948b442ab7b687f967814a7d7f000.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-f5fdcb1d2e599664c34142dd912464640ce459d4.css" media="screen" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-5dcdaf734c8092261f37e6534c8f114696d913a9.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-c45736bc9622ede1d9e87034c4341cda7f90bed5.js" type="text/javascript"></script>
      

        <link rel='permalink' href='/Snowlinux/snowMount/blob/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py'>
    <meta property="og:title" content="snowMount"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/Snowlinux/snowMount"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/db881db43b204513a3227d1051562a8b?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="A GUI for editing mounts (/etc/fstab). Contribute to snowMount development by creating an account on GitHub."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="Snowlinux/snowMount"/>

    <meta name="description" content="A GUI for editing mounts (/etc/fstab). Contribute to snowMount development by creating an account on GitHub." />

  <link href="https://github.com/Snowlinux/snowMount/commits/d4c918ce836f98b6b80597f93e261b79d1d06fc3.atom" rel="alternate" title="Recent Commits to snowMount:d4c918ce836f98b6b80597f93e261b79d1d06fc3" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob linux vis-public env-production  ">
    <div id="wrapper">

      

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1360648843" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1360648843" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary" href="https://github.com/signup">Sign up for free</a>
              <a class="button" href="https://github.com/login?return_to=%2FSnowlinux%2FsnowMount%2Fblob%2Fd4c918ce836f98b6b80597f93e261b79d1d06fc3%2FsnowMount.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu">
          <div class="container">
            <div class="title-actions-bar">
              


<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2FSnowlinux%2FsnowMount"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/Snowlinux/snowMount/stargazers">
        0
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2FSnowlinux%2FsnowMount"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/Snowlinux/snowMount/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/Snowlinux" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">Snowlinux</span>
                  </a></span> /
                <strong><a href="/Snowlinux/snowMount" class="js-current-repository">snowMount</a></strong>
              </h1>
            </div>

            

  <ul class="tabs">
    <li><a href="/Snowlinux/snowMount" class="selected" highlight="[:repo_source, :repo_downloads, :repo_commits, :repo_tags, :repo_branches]">Code</a></li>
    <li><a href="/Snowlinux/snowMount/network" highlight="[:repo_network]">Network</a></li>
    <li><a href="/Snowlinux/snowMount/pulls" highlight="[:repo_pulls]">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/Snowlinux/snowMount/issues" highlight="[:repo_issues]">Issues <span class='counter'>0</span></a></li>



    <li><a href="/Snowlinux/snowMount/graphs" highlight="[:repo_graphs, :repo_contributors]">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/Snowlinux/snowMount/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="">
        <span class="mini-icon mini-icon-tree"></span>
        <i>tree:</i>
        <span class="js-select-button">d4c918ce83</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container js-select-menu-pane">

        <div class="select-menu-modal js-select-menu-pane">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-select-menu-text-filter js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div> <!-- /.select-menu-text-filter -->
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches" data-filterable-for="commitish-filter-field" data-filterable-type="substring">


              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-checkmark mini-icon mini-icon-confirm"></span>
                <a href="/Snowlinux/snowMount/blob/master/snowMount.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
              </div> <!-- /.select-menu-item -->

              <div class="select-menu-no-results js-not-filterable">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags" data-filterable-for="commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-no-results js-not-filterable">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/Snowlinux/snowMount" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/Snowlinux/snowMount/commits/" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/Snowlinux/snowMount/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:9d73e93fef0fc2a662748e669a5f4f61 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:9d73e93fef0fc2a662748e669a5f4f61 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Snowlinux/snowMount/tree/d4c918ce836f98b6b80597f93e261b79d1d06fc3" class="js-slide-to" data-direction="back" itemscope="url" rel="nofollow"><span itemprop="title">snowMount</span></a></span></span> / <strong class="final-path">snowMount.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="snowMount.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/Snowlinux/snowMount/find/d4c918ce836f98b6b80597f93e261b79d1d06fc3" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/23956a8aa6332d9cbccea1d455a7bfcf?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><span rel="author">Lars Torben Kremer</span></span>
    <time class="js-relative-date" datetime="2013-02-17T13:47:37-08:00" title="2013-02-17 13:47:37">February 17, 2013</time>
    <div class="commit-title">
        <a href="/Snowlinux/snowMount/commit/d4c918ce836f98b6b80597f93e261b79d1d06fc3" class="message">Apply &gt; Save</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>2</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="ajacobsen" href="/Snowlinux/snowMount/commits/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py?author=ajacobsen"><img height="20" src="https://secure.gravatar.com/avatar/ad20f108f5f8b7528472a8b7a5bf8fbf?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="dalcde" href="/Snowlinux/snowMount/commits/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py?author=dalcde"><img height="20" src="https://secure.gravatar.com/avatar/ab74c6482abb18012ffd863ec084bc01?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/ad20f108f5f8b7528472a8b7a5bf8fbf?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/ajacobsen">ajacobsen</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/ab74c6482abb18012ffd863ec084bc01?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/dalcde">dalcde</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/Snowlinux/snowMount/blob/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py" data-title="snowMount/snowMount.py at d4c918ce836f98b6b80597f93e261b79d1d06fc3 · Snowlinux/snowMount · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>371 lines (318 sloc)</span>
                <span>14.365 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/Snowlinux/snowMount/raw/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/Snowlinux/snowMount/blame/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py" class="button minibutton ">Blame</a>
                  <a href="/Snowlinux/snowMount/commits/d4c918ce836f98b6b80597f93e261b79d1d06fc3/snowMount.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="data type-python js-blob-data">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
</pre>
          </td>
          <td width="100%">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC4'><span class="kn">import</span> <span class="nn">re</span></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">commands</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">gi.repository</span> <span class="kn">import</span> <span class="n">Gtk</span><span class="p">,</span> <span class="n">Gio</span></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><span class="n">DEBUG</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC12'><span class="n">FSTAB_PATH</span> <span class="o">=</span> <span class="s">&#39;/etc/fstab&#39;</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="c">##################################################</span></div><div class='line' id='LC15'><span class="c">#                  Drive Reader                  #</span></div><div class='line' id='LC16'><span class="c">##################################################</span></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'><span class="k">def</span> <span class="nf">write_fstab</span><span class="p">(</span><span class="n">fstab</span><span class="p">):</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">file_header</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;# /etc/fstab - generated with snowMount</span></div><div class='line' id='LC20'><span class="s">#</span></div><div class='line' id='LC21'><span class="s"># Use &#39;blkid&#39; to print the universally unique identifier for a</span></div><div class='line' id='LC22'><span class="s"># device; this may be used with UUID= as a more robust way to name devices</span></div><div class='line' id='LC23'><span class="s"># that works even if disks are added and removed. See fstab(5).</span></div><div class='line' id='LC24'><span class="s">#</span></div><div class='line' id='LC25'><span class="s"># &lt;file system&gt;</span><span class="se">\t</span><span class="s">&lt;mount point&gt;</span><span class="se">\t</span><span class="s">&lt;type&gt;</span><span class="se">\t</span><span class="s">&lt;options&gt;</span><span class="se">\t</span><span class="s">&lt;dump&gt;</span><span class="se">\t</span><span class="s">&lt;pass&gt;&#39;&#39;&#39;</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">fstab</span><span class="p">:</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;use_uuid&#39;</span><span class="p">]:</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_line</span> <span class="o">=</span> <span class="s">&#39;UUID={}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_spec&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_file&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_vfstype&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_mntops&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_freq&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_passno&#39;</span><span class="p">])</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_line</span> <span class="o">=</span> <span class="s">&#39;{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\t</span><span class="s">{}</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_spec&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_file&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_vfstype&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_mntops&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_freq&#39;</span><span class="p">],</span> <span class="n">fstab</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="s">&#39;fs_passno&#39;</span><span class="p">])</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_line</span><span class="p">)</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output</span> <span class="o">=</span> <span class="s">&#39;{}</span><span class="se">\n</span><span class="s">{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">file_header</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">))</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">FSTAB_PATH</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="nb">file</span><span class="p">:</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">output</span><span class="p">)</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">IOError</span><span class="p">,</span> <span class="n">detail</span><span class="p">:</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">detail</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'><span class="k">def</span> <span class="nf">read_fstab</span><span class="p">():</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Returns a dict like this:</span></div><div class='line' id='LC42'><span class="sd">    &#39;/dev/sda1&#39;: {&#39;fs_file&#39;: &#39;/&#39;,</span></div><div class='line' id='LC43'><span class="sd">                &#39;fs_freq&#39;: &#39;0&#39;,</span></div><div class='line' id='LC44'><span class="sd">                &#39;fs_mntops&#39;: &#39;errors=remount-ro&#39;,</span></div><div class='line' id='LC45'><span class="sd">                &#39;fs_passno&#39;: &#39;1&#39;,</span></div><div class='line' id='LC46'><span class="sd">                &#39;fs_spec&#39;: &#39;f8b392f2-4b9e-4a12-aa40-3b40817e99f3&#39;,</span></div><div class='line' id='LC47'><span class="sd">                &#39;fs_vfstype&#39;: &#39;ext4&#39;}</span></div><div class='line' id='LC48'><span class="sd">    &#39;/dev/sda3&#39;: {&#39;fs_file&#39;: &#39;/home&#39;,</span></div><div class='line' id='LC49'><span class="sd">                &#39;fs_freq&#39;: &#39;0&#39;,</span></div><div class='line' id='LC50'><span class="sd">                &#39;fs_mntops&#39;: &#39;defaults&#39;,</span></div><div class='line' id='LC51'><span class="sd">                &#39;fs_passno&#39;: &#39;2&#39;,</span></div><div class='line' id='LC52'><span class="sd">                &#39;fs_spec&#39;: &#39;dd682fd8-81e0-4ab0-8bc6-54164af8171d&#39;,</span></div><div class='line' id='LC53'><span class="sd">                &#39;fs_vfstype&#39;: &#39;ext4&#39;}&#39;&#39;&#39;</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">devices</span> <span class="o">=</span> <span class="n">get_devices</span><span class="p">()</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">FSTAB_PATH</span><span class="p">)</span> <span class="k">as</span> <span class="n">lines</span><span class="p">:</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;#&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">():</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;UUID&#39;</span><span class="p">):</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">device</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">check_output</span><span class="p">([</span><span class="s">&#39;blkid&#39;</span><span class="p">,</span> <span class="s">&#39;-U&#39;</span><span class="p">,</span> <span class="n">fs_spec</span><span class="p">])</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;LABEL&#39;</span><span class="p">):</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">label</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">device</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">check_output</span><span class="p">([</span><span class="s">&#39;blkid&#39;</span><span class="p">,</span> <span class="s">&#39;-L&#39;</span><span class="p">,</span> <span class="n">label</span><span class="p">])</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">devices</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;UUID&#39;</span><span class="p">]</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;/dev/&#39;</span><span class="p">):</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">device</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">devices</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;UUID&#39;</span><span class="p">]</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">device</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC81'><br/></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_file</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_vfstype</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_mntops</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">3</span><span class="p">]</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_freq</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">4</span><span class="p">]</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_passno</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">5</span><span class="p">]</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;fs_spec&#39;</span> <span class="p">:</span> <span class="n">fs_spec</span><span class="p">,</span> <span class="s">&#39;fs_file&#39;</span> <span class="p">:</span> <span class="n">fs_file</span><span class="p">,</span> <span class="s">&#39;fs_vfstype&#39;</span> <span class="p">:</span> <span class="n">fs_vfstype</span><span class="p">,</span> <span class="s">&#39;fs_mntops&#39;</span> <span class="p">:</span> <span class="n">fs_mntops</span><span class="p">,</span> <span class="s">&#39;fs_freq&#39;</span> <span class="p">:</span> <span class="n">fs_freq</span><span class="p">,</span> <span class="s">&#39;fs_passno&#39;</span> <span class="p">:</span> <span class="n">fs_passno</span><span class="p">,</span> <span class="s">&#39;use_uuid&#39;</span> <span class="p">:</span> <span class="n">use_uuid</span><span class="p">}</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fstab</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">IOError</span><span class="p">,</span> <span class="n">detail</span><span class="p">:</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">detail</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'><span class="k">def</span> <span class="nf">get_devices</span><span class="p">():</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Returns a dict like this:</span></div><div class='line' id='LC94'><span class="sd">    &#39;/dev/sda1&#39;: {&#39;LABEL&#39;: &#39;&quot;root&quot;&#39;,</span></div><div class='line' id='LC95'><span class="sd">                &#39;TYPE&#39;: &#39;&quot;ext4&quot;&#39;,</span></div><div class='line' id='LC96'><span class="sd">                &#39;UUID&#39;: &#39;&quot;f8b392f2-4b9e-4a12-aa40-3b40817e99f3&quot;&#39;},</span></div><div class='line' id='LC97'><span class="sd">    &#39;/dev/sda2&#39;: {&#39;TYPE&#39;: &#39;&quot;swap&quot;&#39;,</span></div><div class='line' id='LC98'><span class="sd">                &#39;UUID&#39;: &#39;&quot;a3cebf99-3cae-4aa4-8c95-832afd565677&quot;&#39;}&#39;&#39;&#39;</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s">&#39;/proc/partitions&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">lines</span><span class="p">:</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="p">(</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">r&#39;sd[a-z][0-9]+&#39;</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">device_names</span> <span class="o">=</span> <span class="p">([</span><span class="n">match</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">results</span> <span class="k">if</span> <span class="n">match</span><span class="p">])</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">dict</span><span class="p">((</span><span class="s">&#39;/dev/{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">device</span><span class="p">),</span> <span class="n">_get_device</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;/dev/&#39;</span><span class="p">,</span> <span class="n">device</span><span class="p">)))</span> <span class="k">for</span> <span class="n">device</span> <span class="ow">in</span> <span class="n">device_names</span><span class="p">)</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">IOError</span><span class="p">,</span> <span class="n">detail</span><span class="p">:</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">detail</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><span class="k">def</span> <span class="nf">_get_device</span><span class="p">(</span><span class="n">device</span><span class="p">):</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">check_output</span><span class="p">([</span><span class="s">&#39;lsblk&#39;</span><span class="p">,</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;-Po&#39;</span><span class="p">,</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;UUID,LABEL,SIZE,TYPE,FSTYPE&#39;</span><span class="p">,</span> <span class="n">device</span><span class="p">])</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">)</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">output</span><span class="p">)</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">detail</span><span class="p">:</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">detail</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><span class="k">def</span> <span class="nf">get_mountpoint</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">fstab</span><span class="p">):</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">device</span> <span class="ow">in</span> <span class="n">fstab</span><span class="p">:</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;fs_file&#39;</span><span class="p">]</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'><span class="k">def</span> <span class="nf">update_fstab</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">mountpoint</span><span class="p">,</span> <span class="n">mountoptions</span><span class="p">,</span> <span class="n">fstab</span><span class="p">):</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mountpoint</span> <span class="o">==</span> <span class="s">&#39;&#39;</span><span class="p">:</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">del</span> <span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">]</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fstab</span></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mountpoint</span> <span class="o">!=</span> <span class="s">&#39;none&#39;</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">mountpoint</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">):</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Invalid mountpoint {}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">mountpoint</span><span class="p">))</span></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mountpoint</span> <span class="o">!=</span> <span class="s">&#39;none&#39;</span> <span class="ow">and</span> <span class="n">mountpoint</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">):</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">mountpoint</span><span class="p">):</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">mountpoint</span><span class="p">)</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">device</span> <span class="ow">in</span> <span class="n">fstab</span><span class="p">:</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;fs_file&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">mountpoint</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mountoptions</span> <span class="o">!=</span> <span class="s">&#39;&#39;</span><span class="p">:</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;fs_mntops&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">mountoptions</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;fs_mntops&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;defaults&#39;</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">devinfo</span> <span class="o">=</span> <span class="n">_get_device</span><span class="p">(</span><span class="n">device</span><span class="p">)</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">devinfo</span><span class="p">[</span><span class="s">&#39;UUID&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">)</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_spec</span> <span class="o">=</span> <span class="n">device</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_uuid</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_file</span> <span class="o">=</span> <span class="n">mountpoint</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_vfstype</span> <span class="o">=</span> <span class="n">devinfo</span><span class="p">[</span><span class="s">&#39;FSTYPE&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">)</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_mntops</span> <span class="o">=</span> <span class="s">&#39;defaults&#39;</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_freq</span> <span class="o">=</span> <span class="s">&#39;0&#39;</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_passno</span> <span class="o">=</span> <span class="s">&#39;0&#39;</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;fs_spec&#39;</span> <span class="p">:</span> <span class="n">fs_spec</span><span class="p">,</span> <span class="s">&#39;fs_file&#39;</span> <span class="p">:</span> <span class="n">fs_file</span><span class="p">,</span> <span class="s">&#39;fs_vfstype&#39;</span> <span class="p">:</span> <span class="n">fs_vfstype</span><span class="p">,</span> <span class="s">&#39;fs_mntops&#39;</span> <span class="p">:</span> <span class="n">fs_mntops</span><span class="p">,</span> <span class="s">&#39;fs_freq&#39;</span> <span class="p">:</span> <span class="n">fs_freq</span><span class="p">,</span> <span class="s">&#39;fs_passno&#39;</span> <span class="p">:</span> <span class="n">fs_passno</span><span class="p">,</span> <span class="s">&#39;use_uuid&#39;</span> <span class="p">:</span> <span class="n">use_uuid</span><span class="p">}</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fstab</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'><span class="k">def</span> <span class="nf">get_fstype</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">fstab</span><span class="p">):</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">device</span> <span class="ow">in</span> <span class="n">fstab</span><span class="p">:</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;fs_vfstype&#39;</span><span class="p">]</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_get_device</span><span class="p">(</span><span class="n">device</span><span class="p">)[</span><span class="s">&#39;FSTYPE&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">)</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'><span class="k">def</span> <span class="nf">get_size</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">devices</span><span class="p">):</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">devices</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;SIZE&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">)</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><span class="k">def</span> <span class="nf">get_mountoptions</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">fstab</span><span class="p">):</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">device</span> <span class="ow">in</span> <span class="n">fstab</span><span class="p">:</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fstab</span><span class="p">[</span><span class="n">device</span><span class="p">][</span><span class="s">&#39;fs_mntops&#39;</span><span class="p">]</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;defaults&#39;</span></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'><span class="c">##################################################</span></div><div class='line' id='LC178'><span class="c">#                  Main Window                   #</span></div><div class='line' id='LC179'><span class="c">##################################################</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'><span class="k">class</span> <span class="nc">MainWindow</span><span class="p">(</span><span class="n">Gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">devices</span><span class="p">,</span> <span class="n">fstab</span><span class="p">):</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">devices</span> <span class="o">=</span> <span class="n">devices</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fstab</span> <span class="o">=</span> <span class="n">fstab</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s">&#39;SnowMount&#39;</span><span class="p">)</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">main_vbox</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Box</span><span class="p">(</span><span class="n">orientation</span><span class="o">=</span><span class="n">Gtk</span><span class="o">.</span><span class="n">Orientation</span><span class="o">.</span><span class="n">VERTICAL</span><span class="p">)</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">main_vbox</span><span class="p">)</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">UI_INFO</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC193'><span class="s">        &lt;ui&gt;</span></div><div class='line' id='LC194'><span class="s">          &lt;menubar name=&#39;MenuBar&#39;&gt;</span></div><div class='line' id='LC195'><span class="s">            &lt;menu action=&#39;FileMenu&#39;&gt;</span></div><div class='line' id='LC196'><span class="s">              &lt;menuitem action=&#39;FileQuit&#39; /&gt;</span></div><div class='line' id='LC197'><span class="s">            &lt;/menu&gt;</span></div><div class='line' id='LC198'><span class="s">            &lt;menu action=&#39;HelpMenu&#39;&gt;</span></div><div class='line' id='LC199'><span class="s">              &lt;menuitem action=&#39;About&#39; /&gt;</span></div><div class='line' id='LC200'><span class="s">            &lt;/menu&gt;</span></div><div class='line' id='LC201'><span class="s">          &lt;/menubar&gt;</span></div><div class='line' id='LC202'><span class="s">        &lt;/ui&gt;</span></div><div class='line' id='LC203'><span class="s">        &quot;&quot;&quot;</span></div><div class='line' id='LC204'><br/></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_group</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">ActionGroup</span><span class="p">(</span><span class="s">&#39;my_actions&#39;</span><span class="p">)</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">add_file_menu_actions</span><span class="p">(</span><span class="n">action_group</span><span class="p">)</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">add_help_menu_actions</span><span class="p">(</span><span class="n">action_group</span><span class="p">)</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uimanager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_ui_manager</span><span class="p">()</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uimanager</span><span class="o">.</span><span class="n">insert_action_group</span><span class="p">(</span><span class="n">action_group</span><span class="p">)</span></div><div class='line' id='LC211'><br/></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">menubar</span> <span class="o">=</span> <span class="n">uimanager</span><span class="o">.</span><span class="n">get_widget</span><span class="p">(</span><span class="s">&#39;/MenuBar&#39;</span><span class="p">)</span></div><div class='line' id='LC213'><br/></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">main_vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">menubar</span><span class="p">,</span> <span class="bp">False</span><span class="p">,</span> <span class="bp">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC215'><br/></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">main_hbox</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Box</span><span class="p">(</span><span class="n">orientation</span><span class="o">=</span><span class="n">Gtk</span><span class="o">.</span><span class="n">Orientation</span><span class="o">.</span><span class="n">HORIZONTAL</span><span class="p">)</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">main_vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">main_hbox</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">device_store</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">ListStore</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">device</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">devices</span><span class="p">:</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">device_store</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">device</span><span class="p">])</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">device_view</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">TreeView</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">device_store</span><span class="p">)</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">device_store_selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">device_view</span><span class="o">.</span><span class="n">get_selection</span><span class="p">()</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">device_store_selection</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;changed&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_cursor_changed</span><span class="p">)</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">renderer</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">CellRendererText</span><span class="p">()</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">column</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">TreeViewColumn</span><span class="p">(</span><span class="s">&quot;Devices&quot;</span><span class="p">,</span> <span class="n">renderer</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">device_view</span><span class="o">.</span><span class="n">append_column</span><span class="p">(</span><span class="n">column</span><span class="p">)</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">main_hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">device_view</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">vbox</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Box</span><span class="p">(</span><span class="n">orientation</span><span class="o">=</span><span class="n">Gtk</span><span class="o">.</span><span class="n">Orientation</span><span class="o">.</span><span class="n">VERTICAL</span><span class="p">)</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">main_hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">vbox</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">frame</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Frame</span><span class="p">(</span><span class="n">label</span><span class="o">=</span><span class="s">&#39;sdXY&#39;</span><span class="p">)</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">frame</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="mi">6</span><span class="p">)</span></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Grid</span><span class="p">(</span><span class="n">column_spacing</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">row_spacing</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">frame</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="p">)</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">label_size</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Size: &#39;</span><span class="p">)</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_size</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_size</span><span class="o">.</span><span class="n">set_editable</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">label_fstype</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Filesystem: &#39;</span><span class="p">)</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_fstype</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_fstype</span><span class="o">.</span><span class="n">set_editable</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">label_mountpoint</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Mountpoint: &#39;</span><span class="p">)</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_mountpoint</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_mountpoint</span><span class="o">.</span><span class="n">set_editable</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">label_mountoptions</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Options: &#39;</span><span class="p">)</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_mountoptions</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_mountoptions</span><span class="o">.</span><span class="n">set_editable</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC251'><br/></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label_size</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entry_size</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label_fstype</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entry_fstype</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label_mountpoint</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entry_mountpoint</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label_mountoptions</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">grid</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entry_mountoptions</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC260'><br/></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">buttonbox</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">ButtonBox</span><span class="p">()</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">button_save</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="s">&#39;Save&#39;</span><span class="p">,</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">STOCK_SAVE</span><span class="p">)</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">button_save</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;clicked&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_button_save_clicked</span><span class="p">)</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">buttonbox</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">button_save</span><span class="p">)</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">buttonbox</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC267'><br/></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">on_cursor_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">selection</span><span class="p">):</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">model</span><span class="p">,</span> <span class="n">treeiter</span> <span class="o">=</span> <span class="n">selection</span><span class="o">.</span><span class="n">get_selected</span><span class="p">()</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">treeiter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">device</span> <span class="o">=</span> <span class="n">model</span><span class="p">[</span><span class="n">treeiter</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">frame</span><span class="o">.</span><span class="n">set_label</span><span class="p">(</span><span class="n">device</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;/dev/&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">))</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_size</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">get_size</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">devices</span><span class="p">))</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_fstype</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">get_fstype</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fstab</span><span class="p">))</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_mountpoint</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">get_mountpoint</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fstab</span><span class="p">))</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">entry_mountoptions</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">get_mountoptions</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fstab</span><span class="p">))</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">current_device</span> <span class="o">=</span> <span class="n">device</span></div><div class='line' id='LC278'><br/></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">on_button_save_clicked</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">):</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mountpoint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entry_mountpoint</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mountoptions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entry_mountoptions</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_fstab</span> <span class="o">=</span> <span class="n">update_fstab</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_device</span><span class="p">,</span> <span class="n">mountpoint</span><span class="p">,</span> <span class="n">mountoptions</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fstab</span><span class="p">)</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">new_fstab</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fstab</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">new_fstab</span><span class="p">)</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">write_fstab</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fstab</span><span class="p">)</span></div><div class='line' id='LC287'><br/></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">detail</span><span class="p">:</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">MessageType</span><span class="o">.</span><span class="n">ERROR</span><span class="p">,</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Gtk</span><span class="o">.</span><span class="n">ButtonsType</span><span class="o">.</span><span class="n">OK</span><span class="p">,</span> <span class="s">&quot;Error!&quot;</span><span class="p">)</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">format_secondary_text</span><span class="p">(</span><span class="n">detail</span><span class="p">)</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">run</span><span class="p">()</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span></div><div class='line' id='LC294'><br/></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">add_file_menu_actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action_group</span><span class="p">):</span></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_filemenu</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Action</span><span class="p">(</span><span class="s">&quot;FileMenu&quot;</span><span class="p">,</span> <span class="s">&quot;File&quot;</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_group</span><span class="o">.</span><span class="n">add_action</span><span class="p">(</span><span class="n">action_filemenu</span><span class="p">)</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_filequit</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">Action</span><span class="p">(</span><span class="s">&quot;FileQuit&quot;</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">STOCK_QUIT</span><span class="p">)</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_filequit</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;activate&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_menu_file_quit</span><span class="p">)</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_group</span><span class="o">.</span><span class="n">add_action</span><span class="p">(</span><span class="n">action_filequit</span><span class="p">)</span></div><div class='line' id='LC301'><br/></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">add_help_menu_actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action_group</span><span class="p">):</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action_group</span><span class="o">.</span><span class="n">add_actions</span><span class="p">([(</span><span class="s">&quot;HelpMenu&quot;</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&quot;Help&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s">&quot;About&quot;</span><span class="p">,</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">STOCK_ABOUT</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_menu_help_about</span><span class="p">)])</span></div><div class='line' id='LC304'><br/></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">create_ui_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uimanager</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">UIManager</span><span class="p">()</span></div><div class='line' id='LC307'><br/></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Throws exception if something went wrong</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uimanager</span><span class="o">.</span><span class="n">add_ui_from_string</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">UI_INFO</span><span class="p">)</span></div><div class='line' id='LC310'><br/></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Add the accelerator group to the toplevel window</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">accelgroup</span> <span class="o">=</span> <span class="n">uimanager</span><span class="o">.</span><span class="n">get_accel_group</span><span class="p">()</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">add_accel_group</span><span class="p">(</span><span class="n">accelgroup</span><span class="p">)</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">uimanager</span></div><div class='line' id='LC315'><br/></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">on_menu_file_quit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">):</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">()</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">on_menu_help_about</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">):</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span> <span class="o">=</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">AboutDialog</span><span class="p">()</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">set_program_name</span><span class="p">(</span><span class="s">&#39;SnowMount&#39;</span><span class="p">)</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">set_version</span><span class="p">(</span><span class="n">VERSION</span><span class="p">)</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">set_license</span><span class="p">(</span><span class="n">LICENSE</span><span class="p">)</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">set_copyright</span><span class="p">(</span><span class="n">COPYRIGHT</span><span class="p">)</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">set_comments</span><span class="p">(</span><span class="s">&#39;A tool to manage mountpoints and options of devices.&#39;</span><span class="p">)</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">run</span><span class="p">()</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dialog</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span></div><div class='line' id='LC328'><br/></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">on_button_press_event</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Check if right mouse button was preseed</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">type</span> <span class="o">==</span> <span class="n">Gdk</span><span class="o">.</span><span class="n">EventType</span><span class="o">.</span><span class="n">BUTTON_PRESS</span> <span class="ow">and</span> <span class="n">event</span><span class="o">.</span><span class="n">button</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">popup</span><span class="o">.</span><span class="n">popup</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">button</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">time</span><span class="p">)</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span> <span class="c"># event has been handled</span></div><div class='line' id='LC334'><br/></div><div class='line' id='LC335'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">getuid</span><span class="p">()</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Please run SnowMount as root.&quot;</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC339'><br/></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">VERSION</span> <span class="o">=</span> <span class="n">commands</span><span class="o">.</span><span class="n">getoutput</span><span class="p">(</span><span class="s">&quot;/usr/lib/snowlinux/common/version.py snowmount&quot;</span><span class="p">)</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">COPYRIGHT</span> <span class="o">=</span> <span class="s">&#39;Copyright (C) 2012,2013  Andy Jacobsen &lt;andy@snowlinux.de&gt;&#39;</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LICENSE</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;This program is free software: you can redistribute it and/or modify</span></div><div class='line' id='LC343'><span class="s">it under the terms of the GNU General Public License as published by</span></div><div class='line' id='LC344'><span class="s">the Free Software Foundation, either version 2 of the License, or</span></div><div class='line' id='LC345'><span class="s">(at your option) any later version.</span></div><div class='line' id='LC346'><br/></div><div class='line' id='LC347'><span class="s">This program is distributed in the hope that it will be useful,</span></div><div class='line' id='LC348'><span class="s">but WITHOUT ANY WARRANTY; without even the implied warranty of</span></div><div class='line' id='LC349'><span class="s">MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></div><div class='line' id='LC350'><span class="s">GNU General Public License for more details.</span></div><div class='line' id='LC351'><span class="s">You should have received a copy of the GNU General Public License</span></div><div class='line' id='LC352'><span class="s">along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.&#39;&#39;&#39;</span></div><div class='line' id='LC353'><br/></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&quot;--version&quot;</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span> <span class="ow">or</span> <span class="s">&quot;-v&quot;</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">:</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;SnowMount version &quot;</span> <span class="o">+</span> <span class="n">VERSION</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">()</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&quot;--dry-run&quot;</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">:</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DEBUG</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">FSTAB_PATH</span> <span class="o">=</span> <span class="s">&#39;/tmp/fstab&#39;</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">FSTAB_PATH</span><span class="p">):</span></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s">&#39;cp /etc/fstab /tmp/&#39;</span><span class="p">)</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fstab</span> <span class="o">=</span> <span class="n">read_fstab</span><span class="p">()</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">devices</span> <span class="o">=</span> <span class="n">get_devices</span><span class="p">()</span></div><div class='line' id='LC365'><br/></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">win</span> <span class="o">=</span> <span class="n">MainWindow</span><span class="p">(</span><span class="n">devices</span><span class="p">,</span> <span class="n">fstab</span><span class="p">)</span></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">win</span><span class="o">.</span><span class="n">set_size_request</span><span class="p">(</span><span class="mi">450</span><span class="p">,</span> <span class="mi">250</span><span class="p">)</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">win</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;delete-event&quot;</span><span class="p">,</span> <span class="n">Gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span></div><div class='line' id='LC369'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">win</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1360648843" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.06298s from fe3.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/Snowlinux/snowMount/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.06364' data-host='fe3'></span>
    
  </body>
</html>

