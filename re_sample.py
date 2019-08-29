
import requests
import re

content = requests.get('http://book.douban.com').text
print(content)
"""
content = '''<body>
    
  <script>var _body_start = new Date();</script>
  
  



    <link href="//img3.doubanio.com/dae/accounts/resources/0246c88/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=book" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="on">
      <a href="https://book.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/0246c88/shire/bundle.js" defer="defer"></script>




  



    <link href="//img3.doubanio.com/dae/accounts/resources/0246c88/book/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;book.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual/2018?source=navigation"
            target="_blank"
     >2018年度榜单</a>
    </li>
    <li    ><a href="https://www.douban.com/standbyme/2018?source=navigation"
            target="_blank"
     >2018书影音报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?biz_type=book&utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

    <a href="https://book.douban.com/annual/2018?source=book_navigation" class="bookannual2018"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/0246c88/book/bundle.js" defer="defer"></script>





  <div id="wrapper">
    
  <!-- douban ad begin -->
  <div id="dale_book_home_top_super_banner" class="ad-placeholder" style="margin: -18px 0 0;">
  </div>
  <!-- douban ad end -->

    
  <div id="content">
    

    <div class="grid-16-8 clearfix">
      
      <div class="article">
  
  

  
  
  <div class="section books-express ">
    <div class="hd">
      
  <h2 class=''>
    <span class="">新书速递</span>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
          >更多»</a>
      </span>
  </h2>

      <div class="slide-controls">
        <ol class="slide-dots">
          <li><a data-index="1" href="#" class=""></a></li>
          <li><a data-index="2" href="#" class=""></a></li>
          <li><a data-index="3" href="#" class=""></a></li>
          <li><a data-index="4" href="#" class=""></a></li>
        </ol>
        <div class="slide-btns">
          <a href="#" class="prev">&#8249;</a>
          <a href="#" class="next">&#8250;</a>
        </div>
      </div>
    </div>
    <div class="bd">
      <div class="carousel">
        <div class="slide-list">
          
  
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30258607/?icn=index-latestbook-subject" title="垂死的肉身">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29979964.jpg" class=""
                  width="115px" height="172px" alt="垂死的肉身">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30258607/?icn=index-latestbook-subject"
                  title="垂死的肉身">垂死的肉身</a>
              </div>
              <div class="author">
                [美] 菲利普·罗斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  垂死的肉身
                </h4>
                <p>
                  <span class="author">
                    [美] 菲利普·罗斯
                  </span>
                  /
                  <span class="year">
                    2019-1-31
                  </span>
                  /
                  <span class="publisher">
                    上海译文出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ◆ 一则虔诚的肉体之爱的神话，如冰中之火，绝望而温暖
∽ ∽ ∽
《垂死的肉身》讲述了年过六旬的美国教授大卫•凯普什与他的学生——二十四岁的古巴女孩康秀拉——发生的一段不寻常的爱欲关系。凯普什迷恋于康秀拉的身体无法自拔，而对康秀拉而言，他的年龄和地位则合情合理地赋予了她屈服的权利。然而渐渐地，对年龄差距的恐惧、对青春的嫉妒抽走了凯普什的自信，使他...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30219714/?icn=index-latestbook-subject" title="生命是什么">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29952612.jpg" class=""
                  width="115px" height="172px" alt="生命是什么">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30219714/?icn=index-latestbook-subject"
                  title="生命是什么">生命是什么</a>
              </div>
              <div class="author">
                [以色列]埃迪·普罗斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  生命是什么
                </h4>
                <p>
                  <span class="author">
                    [以色列]埃迪·普罗斯
                  </span>
                  /
                  <span class="year">
                    2018-12-1
                  </span>
                  /
                  <span class="publisher">
                    中信出版社·新思文化
                  </span>
                </p>
                <p class="abstract">
                  
                  革新薛定谔同名经典，与《自私的基因》一起入选“牛津科普里程碑”的大师小书。
探寻生命起源的非凡旅程，没有一个公式的诗意科普。
生命是什么，我们是谁，宇宙为何存在……当一个人沉思过生命，就再也无法漠然地生活。
-
【内容简介】
“生命是什么？”当你脑中浮现这个疑问，意味着你来到了物理学、化学、生物学、哲学等人类核心知识的交叉口，也意味着你与亚里士多德...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30457133/?icn=index-latestbook-subject" title="读心师">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30002353.jpg" class=""
                  width="115px" height="172px" alt="读心师">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30457133/?icn=index-latestbook-subject"
                  title="读心师">读心师</a>
              </div>
              <div class="author">
                向林
              </div>
              <div class="more-meta">
                <h4 class="title">
                  读心师
                </h4>
                <p>
                  <span class="author">
                    向林
                  </span>
                  /
                  <span class="year">
                    2019-2-1
                  </span>
                  /
                  <span class="publisher">
                    湖南文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  男子与同学聚会一夜未归，次日清晨，街巷四邻忽闻煮尸异味…… 因与嫌疑人的特殊关系，兼具天才与疯子气质的心理学家沈跃主动加入专案调查组。而煮尸案后，古董失踪案、连环强奸案、吊诡自杀案……陆续浮出水面，如蝴蝶扇动翅膀就引发海啸一般，案件被一步步牵引到几不可控的地步。沈跃和他的犯罪心理小组，再度出发！从看不见的细节嗅出破绽，从不可能的人中觅出真...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30421553/?icn=index-latestbook-subject" title="汪曾祺全集（全十二卷）">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29962218.jpg" class=""
                  width="115px" height="172px" alt="汪曾祺全集（全十二卷）">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30421553/?icn=index-latestbook-subject"
                  title="汪曾祺全集（全十二卷）">汪曾祺全集（全十二卷）</a>
              </div>
              <div class="author">
                汪曾祺&nbsp;/&nbsp;（编辑 ）季红真、刘伟 等
              </div>
              <div class="more-meta">
                <h4 class="title">
                  汪曾祺全集（全十二卷）
                </h4>
                <p>
                  <span class="author">
                    汪曾祺&nbsp;/&nbsp;（编辑 ）季红真、刘伟 等
                  </span>
                  /
                  <span class="year">
                    2019-1-10
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  此次全集的出版以汪先生的手稿作为第一位组稿来源，为呈现出一部更加全面、翔实的《汪曾祺全集》做 了充足准备。
全集还增添了汪先生的书画、对联、戏剧等多项内容。
随着一部全面、翔实又精美的《汪曾祺全集》和广大读者见面，是对已仙逝十余年的汪先生的最好纪念之一。
新版《汪曾祺全集》除小说卷、散文卷、诗歌卷、书信卷外，还包括谈艺卷（收录汪曾祺对于诗歌、京...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30401746/?icn=index-latestbook-subject" title="谍局 1">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29976546.jpg" class=""
                  width="115px" height="172px" alt="谍局 1">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30401746/?icn=index-latestbook-subject"
                  title="谍局 1">谍局 1</a>
              </div>
              <div class="author">
                [日] 松本清张
              </div>
              <div class="more-meta">
                <h4 class="title">
                  谍局 1
                </h4>
                <p>
                  <span class="author">
                    [日] 松本清张
                  </span>
                  /
                  <span class="year">
                    2019-1-1
                  </span>
                  /
                  <span class="publisher">
                    中国工人出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  一个日本女人，拍摄到了美国总统与日本首相秘密会晤的五人合影照片，他们在密谋什么？女人本想拿此照片讹诈一笔钱，然而此时，照片的两人相继死于非命，究竟谁是凶手？
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30338155/?icn=index-latestbook-subject" title="场景">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29965718.jpg" class=""
                  width="115px" height="172px" alt="场景">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30338155/?icn=index-latestbook-subject"
                  title="场景">场景</a>
              </div>
              <div class="author">
                【加】丹尼尔•亚伦•西尔&nbsp;/&nbsp;【美】特里• 尼科尔斯•克拉克
              </div>
              <div class="more-meta">
                <h4 class="title">
                  场景
                </h4>
                <p>
                  <span class="author">
                    【加】丹尼尔•亚伦•西尔&nbsp;/&nbsp;【美】特里• 尼科尔斯•克拉克
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    方寸 | 社会科学文献出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  场景，是一个地方的整体文化风格或美学特征。当一个社区变成一个场景时，它可以成为培养各类精神的地方。场景，正在重新定义城市经济、居住生活、政治活动和公共政策……
《场景：空间品质如何塑造社会生活》一书所介绍的场景理论，由特里•克拉克和丹尼尔•西尔为首的新芝加哥学派创立，是国际上首个分析城市的文化风格和美学特征对城市发展作用的理论工具。从经济增...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30305893/?icn=index-latestbook-subject" title="太阳王与海妖">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29952224.jpg" class=""
                  width="115px" height="172px" alt="太阳王与海妖">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30305893/?icn=index-latestbook-subject"
                  title="太阳王与海妖">太阳王与海妖</a>
              </div>
              <div class="author">
                [美]冯达·N.麦金泰尔
              </div>
              <div class="more-meta">
                <h4 class="title">
                  太阳王与海妖
                </h4>
                <p>
                  <span class="author">
                    [美]冯达·N.麦金泰尔
                  </span>
                  /
                  <span class="year">
                    2019-3-1
                  </span>
                  /
                  <span class="publisher">
                    天地出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★史上最佳架空历史小说！
★击败乔治·马丁《权力的游戏》获得星云奖。
★《出版者周刊》年度图书，《轨迹》杂志推荐图书，入围小詹姆斯·提普垂奖、银河最佳小说奖，日本星云奖提名
★融历史、科学、魔幻、哥特式惊悚于一体的历史言情奇幻小说。
★《地海传奇》系列作者厄休拉·勒奎恩极力推荐。
★改编电影《日月人鱼》由007主演皮尔斯·布洛斯南和范冰冰领衔主演，《...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30426745/?icn=index-latestbook-subject" title="念楼学短">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29972482.jpg" class=""
                  width="115px" height="172px" alt="念楼学短">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30426745/?icn=index-latestbook-subject"
                  title="念楼学短">念楼学短</a>
              </div>
              <div class="author">
                锺叔河
              </div>
              <div class="more-meta">
                <h4 class="title">
                  念楼学短
                </h4>
                <p>
                  <span class="author">
                    锺叔河
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    后浪丨湖南美术出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  53项主题 530篇选文 百字版《古文观止》
传统文化启蒙的优选读物 拉近与经典文言文的距离
读古文，学作文，都应先学其短
◎ 编辑推荐
☆87岁老编辑，69年出版经验
著名出版家锺叔河先生心血力作，为教育孙辈而编纂的古文合集。每篇选文都由锺先生精心拣择，包含文言原文，并有白话翻译【念楼读】和评批【念楼曰】。
☆53项主题，530篇选文
内容横跨多个领域，四书五经、笔...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30390667/?icn=index-latestbook-subject" title="奥斯特利茨">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29951872.jpg" class=""
                  width="115px" height="172px" alt="奥斯特利茨">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30390667/?icn=index-latestbook-subject"
                  title="奥斯特利茨">奥斯特利茨</a>
              </div>
              <div class="author">
                [德]温弗里德•塞巴尔德
              </div>
              <div class="more-meta">
                <h4 class="title">
                  奥斯特利茨
                </h4>
                <p>
                  <span class="author">
                    [德]温弗里德•塞巴尔德
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    广西师范大学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ◉内容简介
人到底需要多少记忆？
当孤身穿过时间，我们真正需要记住什么，面对什么？
一个追寻真相的高贵灵魂，一幅奇异梦幻的记忆拼图，
从威尔士到伦敦到布拉格到巴黎，
一个维特根斯坦式的男子，在理性与罪之间徘徊，
穿越时间之雪，抵达先于身体的伤口。
本书是德国作家温弗里德 •塞巴尔德享誉国际的代表之作，也是其离世前发表的最后一部作品。奥斯特利茨（Austerlitz...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30306717/?icn=index-latestbook-subject" title="希腊罗马神话">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29951129.jpg" class=""
                  width="115px" height="172px" alt="希腊罗马神话">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30306717/?icn=index-latestbook-subject"
                  title="希腊罗马神话">希腊罗马神话</a>
              </div>
              <div class="author">
                [英] 菲利普·马蒂塞克（Philip Matyszak）
              </div>
              <div class="more-meta">
                <h4 class="title">
                  希腊罗马神话
                </h4>
                <p>
                  <span class="author">
                    [英] 菲利普·马蒂塞克（Philip Matyszak）
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    后浪丨民主与建设出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  古典学学者写给大众的神话小书
追溯古希腊罗马神话的前世今生
双色印刷，大量文物、艺术品图片展示
………………
※编辑推荐※
全面介绍古希腊罗马泛神论宗教的神灵体系、民间传说故事和英雄史诗。
作者学养深厚，在介绍那些我们耳熟能详的名字和故事的同时，还在字里行间暗暗勾画出了古代人的信仰系统和内心世界。
文笔严谨而不失幽默感，偶有不动声色的反讽佳句——既传达...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30420900/?icn=index-latestbook-subject" title="奥丽芙·基特里奇">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29993079.jpg" class=""
                  width="115px" height="172px" alt="奥丽芙·基特里奇">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30420900/?icn=index-latestbook-subject"
                  title="奥丽芙·基特里奇">奥丽芙·基特里奇</a>
              </div>
              <div class="author">
                [美] 伊丽莎白·斯特劳特
              </div>
              <div class="more-meta">
                <h4 class="title">
                  奥丽芙·基特里奇
                </h4>
                <p>
                  <span class="author">
                    [美] 伊丽莎白·斯特劳特
                  </span>
                  /
                  <span class="year">
                    2019-3-1
                  </span>
                  /
                  <span class="publisher">
                    南海出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  《奥丽芙·基特里奇》内容简介：
--在儿子的婚礼上，奥丽芙无意中听到新娘说了几句自己的坏话，便赌气偷走她的一只皮鞋，扔进了垃圾桶。
--丈夫送的一束鲜花被奥丽芙毫不在意地丢进了旧花瓶，她没再多看一眼。
--“你娶了一个怪物，可你还是爱她。”奥丽芙始终没有对丈夫说出这句话。
奥丽芙刻薄、暴躁，她拒绝道歉和一切无用的矫情。可在别人看不到的地方，她也会不动声色...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30415665/?icn=index-latestbook-subject" title="文明">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29965795.jpg" class=""
                  width="115px" height="172px" alt="文明">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30415665/?icn=index-latestbook-subject"
                  title="文明">文明</a>
              </div>
              <div class="author">
                [英] 肯尼斯·克拉克
              </div>
              <div class="more-meta">
                <h4 class="title">
                  文明
                </h4>
                <p>
                  <span class="author">
                    [英] 肯尼斯·克拉克
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    理想国丨中国美术学院出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  《文明》首播于1969年，开BBC彩色艺术纪录片之先河。年逾花甲的肯尼斯•克拉克与拍摄人员合作，走访13个国家，拍摄117处地点，行程超过13万千米，堪为典范。《文明》与同名著作一道，汇集了作者毕生对艺术的思考，成为理解欧洲文明与艺术无法绕过的经典。
绘画、雕刻、建筑、文学和音乐是文明最直接的表现。克拉克以其广博的知识和笃定的判断，回顾了欧洲自罗马帝...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30324570/?icn=index-latestbook-subject" title="关于同一个男人简单生活的想象">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29995283.jpg" class=""
                  width="115px" height="172px" alt="关于同一个男人简单生活的想象">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30324570/?icn=index-latestbook-subject"
                  title="关于同一个男人简单生活的想象">关于同一个男人简单生活的想象</a>
              </div>
              <div class="author">
                [丹]海勒·海勒
              </div>
              <div class="more-meta">
                <h4 class="title">
                  关于同一个男人简单生活的想象
                </h4>
                <p>
                  <span class="author">
                    [丹]海勒·海勒
                  </span>
                  /
                  <span class="year">
                    2019-1-1
                  </span>
                  /
                  <span class="publisher">
                    中国国际广播出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  圣诞节前一天的清晨，苏珊娜发现自己的丈夫金姆死在了床上。
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30385026/?icn=index-latestbook-subject" title="购物凶猛">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29943567.jpg" class=""
                  width="115px" height="172px" alt="购物凶猛">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30385026/?icn=index-latestbook-subject"
                  title="购物凶猛">购物凶猛</a>
              </div>
              <div class="author">
                孙骁骥
              </div>
              <div class="more-meta">
                <h4 class="title">
                  购物凶猛
                </h4>
                <p>
                  <span class="author">
                    孙骁骥
                  </span>
                  /
                  <span class="year">
                    2019-2-1
                  </span>
                  /
                  <span class="publisher">
                    东方出版社
                  </span>
                </p>
                <p class="abstract"></p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30217953/?icn=index-latestbook-subject" title="哀愁的预感">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29952684.jpg" class=""
                  width="115px" height="172px" alt="哀愁的预感">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30217953/?icn=index-latestbook-subject"
                  title="哀愁的预感">哀愁的预感</a>
              </div>
              <div class="author">
                [日] 吉本芭娜娜
              </div>
              <div class="more-meta">
                <h4 class="title">
                  哀愁的预感
                </h4>
                <p>
                  <span class="author">
                    [日] 吉本芭娜娜
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    上海译文出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ◆ 治愈，从这里开始。
青春总是以说不清的哀愁揭开序幕
十九岁少女弥生的初夏物语
“最好还是一无所知”之类的说法，根本就说不通。
∽ ∽ ∽
天生异能的少女弥生屡获天启，终于来到了“阿姨”的家——言行乖张古怪的音乐教师雪野就独居在那所充盈着浓浓绿意的古宅里。时间在两人的共处中无声流逝，近乎透明。一个阴翳的下午，雪野的钢琴声在空气里渐行渐远，弥生19岁的初...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30434869/?icn=index-latestbook-subject" title="HBO的内容战略">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30010612.jpg" class=""
                  width="115px" height="172px" alt="HBO的内容战略">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30434869/?icn=index-latestbook-subject"
                  title="HBO的内容战略">HBO的内容战略</a>
              </div>
              <div class="author">
                (美) 小比尔•梅西（Bill Mesce, Jr.）
              </div>
              <div class="more-meta">
                <h4 class="title">
                  HBO的内容战略
                </h4>
                <p>
                  <span class="author">
                    (美) 小比尔•梅西（Bill Mesce, Jr.）
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    湛庐文化/浙江人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ● 电视有两个时代：有HBO的时代与没有HBO的时代。1972年HBO开播，一个全新的娱乐时代来临，电视进入了有HBO的时代。HBO改变了一切，从电视产业本身到电影业的版图，从家庭录像带到网络电视，在1972 年之后发生的所有变化几乎都与HBO 的成功有着直接或间接的关系。
●《HBO的内容战略》详述了HBO的内容战略及其演变。1972年，HBO开播。一开始，作为电影...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30387898/?icn=index-latestbook-subject" title="金色机械">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29987798.jpg" class=""
                  width="115px" height="172px" alt="金色机械">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30387898/?icn=index-latestbook-subject"
                  title="金色机械">金色机械</a>
              </div>
              <div class="author">
                [日] 恒川光太郎
              </div>
              <div class="more-meta">
                <h4 class="title">
                  金色机械
                </h4>
                <p>
                  <span class="author">
                    [日] 恒川光太郎
                  </span>
                  /
                  <span class="year">
                    2019-2
                  </span>
                  /
                  <span class="publisher">
                    化学工业出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★日本科幻大师田中芳树也投了它一票！《金色机械》是日本推理文坛至高荣誉——推理作家协会奖第67回受奖之作。该大奖创立已70年，是日本推理界第一权威的奖项；
★作者恒川光太郎是日本著名的推理、科幻、恐怖小说作家，2005年以《夜市》荣获第十二届“日本恐怖小说大赏”，被誉为是该奖有史以来尤其出色的杰作，惊人的写作才能从此震撼日本文坛。恒川光太郎擅长幻...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30288497/?icn=index-latestbook-subject" title="过剩之地">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29906241.jpg" class=""
                  width="115px" height="172px" alt="过剩之地">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30288497/?icn=index-latestbook-subject"
                  title="过剩之地">过剩之地</a>
              </div>
              <div class="author">
                [美]莫妮卡·普拉萨德
              </div>
              <div class="more-meta">
                <h4 class="title">
                  过剩之地
                </h4>
                <p>
                  <span class="author">
                    [美]莫妮卡·普拉萨德
                  </span>
                  /
                  <span class="year">
                    2019-1-1
                  </span>
                  /
                  <span class="publisher">
                    上海人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  美国道路为何对贫困问题无能为力？“需求侧”经济如何引发今日危机？
揭示美国政府干预的真实面相，避开美国经验的政策陷阱。
斩获美国社会学协会社会学杰出学术贡献等六项大奖
19世纪末美国经济出现了爆炸式增长，而路易斯安那州的传奇州长休伊·朗却质问道：“这是一片超级富足的过剩之地，可为何到处都是食不果腹、衣不蔽体、无家可归的人呢？”
休伊·朗是那个时代...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30398416/?icn=index-latestbook-subject" title="巧合制造师">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29951546.jpg" class=""
                  width="115px" height="172px" alt="巧合制造师">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30398416/?icn=index-latestbook-subject"
                  title="巧合制造师">巧合制造师</a>
              </div>
              <div class="author">
                (以)约夫·布卢姆
              </div>
              <div class="more-meta">
                <h4 class="title">
                  巧合制造师
                </h4>
                <p>
                  <span class="author">
                    (以)约夫·布卢姆
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    中信出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  不经意间打翻的一杯水，拼命追跑也没赶上的一班公车，生活处处有意外，可能是惊喜，也可能是惊吓，偏偏一整天都被打乱。但如果说这些意外都不是巧合呢？
盖伊、艾米丽、埃里克，三位看似平凡的男女正是能够操纵“意外”的“巧合制造师”。在常人眼里的偶然，可能源自他们漫长的精心策划，一次擦肩而过，一场突如其来的停电，都有可能掀起改变世界命运的波澜。随着盖伊...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30418117/?icn=index-latestbook-subject" title="因计算机而强大">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29970195.jpg" class=""
                  width="115px" height="172px" alt="因计算机而强大">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30418117/?icn=index-latestbook-subject"
                  title="因计算机而强大">因计算机而强大</a>
              </div>
              <div class="author">
                [美]西摩 佩珀特 Seymour Papert
              </div>
              <div class="more-meta">
                <h4 class="title">
                  因计算机而强大
                </h4>
                <p>
                  <span class="author">
                    [美]西摩 佩珀特 Seymour Papert
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  本书有两个中心主题——
孩子可以轻松自如地学习使用计算机；
学习使用计算机能够改变他们学习其他知识的方式。 （前苹果公司总裁 约翰·斯卡利）
最有可能带来文化变革的就是计算机的不断普及。
计算机不仅是一个工具，它对我们的心智有着根本和深远的影响。
计算机不仅帮助我们学习 ，还帮助我们学习怎样学习。
计算机是一种调解人与人之间关系的移情对象。
一个数学的头脑...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30325319/?icn=index-latestbook-subject" title="夏日尽处">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29973219.jpg" class=""
                  width="115px" height="172px" alt="夏日尽处">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30325319/?icn=index-latestbook-subject"
                  title="夏日尽处">夏日尽处</a>
              </div>
              <div class="author">
                [荷]荷曼·柯赫(Herman Koch)
              </div>
              <div class="more-meta">
                <h4 class="title">
                  夏日尽处
                </h4>
                <p>
                  <span class="author">
                    [荷]荷曼·柯赫(Herman Koch)
                  </span>
                  /
                  <span class="year">
                    2019-2
                  </span>
                  /
                  <span class="publisher">
                    湖南文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★ 国际IMPAC都柏林文学奖长名单
★ 《出版人周刊》年度小说奖
★ 《纽约时报》畅销书
★ 荷兰获奖作家实力代表作
★ 一名医生在医德与家庭之间的两难抉择。
★ 文明只是对人类本能的一种掩饰。
-------------------------------------------------------
马克是许多名流的家庭医生，善于拿捏人际关系，并引以为傲。人前，他是尽职尽责的完美医生；人后，他自私又伪善，丝毫不在乎病人的痛苦与无...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30389721/?icn=index-latestbook-subject" title="卡帕 : 战地流星">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29962383.jpg" class=""
                  width="115px" height="172px" alt="卡帕 : 战地流星">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30389721/?icn=index-latestbook-subject"
                  title="卡帕 : 战地流星">卡帕 : 战地流星</a>
              </div>
              <div class="author">
                [法] 弗洛朗·西洛雷
              </div>
              <div class="more-meta">
                <h4 class="title">
                  卡帕 : 战地流星
                </h4>
                <p>
                  <span class="author">
                    [法] 弗洛朗·西洛雷
                  </span>
                  /
                  <span class="year">
                    2019-3
                  </span>
                  /
                  <span class="publisher">
                    后浪丨四川文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  “如果你的照片不够好，那是因为你离得不够近。”
——罗伯特·卡帕
他一生纵情声色，却不曾溺于喧嚣，在命运的起承转合中，为一个时代留下了生命的注释……
1913年，卡帕出生于布达佩斯的一个犹太家庭，本名为安德烈·弗里德曼。
1933年，他在巴黎与卡蒂埃-布列松成为同事， 和德国“小红狐”—— 摄影师格尔达·塔罗陷入热恋。
1936年，他和格尔达奔赴西班牙科尔多瓦前...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30261422/?icn=index-latestbook-subject" title="鬼作家">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29980004.jpg" class=""
                  width="115px" height="172px" alt="鬼作家">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30261422/?icn=index-latestbook-subject"
                  title="鬼作家">鬼作家</a>
              </div>
              <div class="author">
                [美] 菲利普·罗斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  鬼作家
                </h4>
                <p>
                  <span class="author">
                    [美] 菲利普·罗斯
                  </span>
                  /
                  <span class="year">
                    2019-1-31
                  </span>
                  /
                  <span class="publisher">
                    上海译文出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  《鬼作家》是内森·祖克曼文学探险系列作品的开篇之作。二十三岁的主人公内森•祖克曼刚出版一批短篇小说，并收到了自己最崇拜的作家E.I. 洛诺夫的邀请，前往对方位于伯克希尔山的家中做客。在那里，内森见到了洛诺夫夫妇与他们收养的一个女学生艾米•贝莱特，他当即被艾米独特的魅力所倾倒。但让内森意想不到的是，在与自己的偶像相处的过程中，对方的妻子霍普突然失...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30437364/?icn=index-latestbook-subject" title="《流浪地球》电影制作手记">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30010216.jpg" class=""
                  width="115px" height="172px" alt="《流浪地球》电影制作手记">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30437364/?icn=index-latestbook-subject"
                  title="《流浪地球》电影制作手记">《流浪地球》电影制作手记</a>
              </div>
              <div class="author">
                朔方
              </div>
              <div class="more-meta">
                <h4 class="title">
                  《流浪地球》电影制作手记
                </h4>
                <p>
                  <span class="author">
                    朔方
                  </span>
                  /
                  <span class="year">
                    2019-3
                  </span>
                  /
                  <span class="publisher">
                    人民交通出版社股份有限公司
                  </span>
                </p>
                <p class="abstract">
                  
                  （1） 雨果奖得主刘慈欣同名小说登录大荧幕，刘慈欣担任电影监制并为本书作序。
（2） 导演郭帆亲自设计封面，“战狼”吴京特别出演。屈楚萧、李光洁、吴孟达、赵今麦领衔主演，雷佳音、宁浩、刘慈欣、郭京飞等客串。
（3）收录电影创作者的心血结晶，内含采访展现电影创作细节，既可作为科幻发烧友的案头珍藏，也能供有心于科幻创作的从业者参考借鉴。
（4） 2019年春...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30371548/?icn=index-latestbook-subject" title="人生最焦虑的就是吃些什么">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29958456.jpg" class=""
                  width="115px" height="172px" alt="人生最焦虑的就是吃些什么">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30371548/?icn=index-latestbook-subject"
                  title="人生最焦虑的就是吃些什么">人生最焦虑的就是吃些什么</a>
              </div>
              <div class="author">
                刘汀
              </div>
              <div class="more-meta">
                <h4 class="title">
                  人生最焦虑的就是吃些什么
                </h4>
                <p>
                  <span class="author">
                    刘汀
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    北京十月文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  一部当代都市人的“吃饭简史”
我们在茫茫人海的北京 进出同一家餐厅
我们选择食物 也选择各自的人生
* * *
本书是作家刘汀的全新小说集，书中收入了六篇小说，每一篇都紧扣书名主题。在这些关于“吃什么”的故事中，有当代北京人的快乐和疲惫，有他们的希望、失望甚至 是绝望 ，也有潜在的救赎，它们紧紧地依附于这座都市的生活经验，折射出时代和社会的反光。全书的各篇小...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30447829/?icn=index-latestbook-subject" title="我是怎样摆平焦虑的">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29993228.jpg" class=""
                  width="115px" height="172px" alt="我是怎样摆平焦虑的">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30447829/?icn=index-latestbook-subject"
                  title="我是怎样摆平焦虑的">我是怎样摆平焦虑的</a>
              </div>
              <div class="author">
                [英] 卡尔·弗农
              </div>
              <div class="more-meta">
                <h4 class="title">
                  我是怎样摆平焦虑的
                </h4>
                <p>
                  <span class="author">
                    [英] 卡尔·弗农
                  </span>
                  /
                  <span class="year">
                    2019-3
                  </span>
                  /
                  <span class="publisher">
                    后浪丨江西人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  在热衷于“贩卖焦虑”的时代
让自己积极地生活下去
英国亚马逊心理自助类销量榜首励志作品
◎ 编辑推荐
☆ 一本更受人喜欢的书
本书荣登英国亚马逊心理自助类销量榜首。作者曾帮助 50 多个国家和地区的人们克服焦虑症，影响力覆盖全球。
☆ 一种更“接地气”的表达
与语言繁冗、堆砌理论的“专家式”作品不同，本书文风口语化，力求幽默好懂，杜绝啰嗦、絮叨和无意义的心灵鸡...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27192522/?icn=index-latestbook-subject" title="星新一少年科幻">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29960457.jpg" class=""
                  width="115px" height="172px" alt="星新一少年科幻">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27192522/?icn=index-latestbook-subject"
                  title="星新一少年科幻">星新一少年科幻</a>
              </div>
              <div class="author">
                [日] 星新一
              </div>
              <div class="more-meta">
                <h4 class="title">
                  星新一少年科幻
                </h4>
                <p>
                  <span class="author">
                    [日] 星新一
                  </span>
                  /
                  <span class="year">
                    2019-1-1
                  </span>
                  /
                  <span class="publisher">
                    安徽少年儿童出版社
                  </span>
                </p>
                <p class="abstract"></p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30320889/?icn=index-latestbook-subject" title="美的进化">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29972505.jpg" class=""
                  width="115px" height="172px" alt="美的进化">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30320889/?icn=index-latestbook-subject"
                  title="美的进化">美的进化</a>
              </div>
              <div class="author">
                [美]理查德·O.普鲁姆（Richard O. Prum）
              </div>
              <div class="more-meta">
                <h4 class="title">
                  美的进化
                </h4>
                <p>
                  <span class="author">
                    [美]理查德·O.普鲁姆（Richard O. Prum）
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    中信出版集团·鹦鹉螺
                  </span>
                </p>
                <p class="abstract">
                  
                  欢迎踏上世界知名鸟类学家理查德·普鲁姆为你量身定制的智力冒险之旅。
我们通常认为达尔文的自然选择理论可以解释生命树上的每一个分支：哪一个物种会繁衍，哪一个物种会灭绝，哪些物种会进化出哪些特征……但是， 达尔文说过：“每当我看到雄孔雀的尾屏，就觉得难受！”这是因为在他的自然选择理论看来，雄孔雀尾屏上过于华丽的图案似乎毫无生存价值。对此，传统科...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30344072/?icn=index-latestbook-subject" title="马戏团离镇">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29971607.jpg" class=""
                  width="115px" height="172px" alt="马戏团离镇">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30344072/?icn=index-latestbook-subject"
                  title="马戏团离镇">马戏团离镇</a>
              </div>
              <div class="author">
                卧斧&nbsp;/&nbsp;伊卡鲁斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  马戏团离镇
                </h4>
                <p>
                  <span class="author">
                    卧斧&nbsp;/&nbsp;伊卡鲁斯
                  </span>
                  /
                  <span class="year">
                    2019-2
                  </span>
                  /
                  <span class="publisher">
                    后浪丨四川人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  唤起童真，拾回初心
一篇探求自我,寻找天堂的童话
卧斧的变奏书写+伊卡鲁斯的奇异绘图
◎ 编辑推荐
★ 鼻子挂墙上的大象、翅膀掉了的空中飞人、没有五官的小丑、不穿衣服的“箱子”……由台湾作家卧斧、绘者伊卡鲁斯合力打造的稀奇古怪马戏团！
★ 孩子参观马戏团经历一连串冒险，像是拼 拼图一般，逐渐接近“事件”的全貌。马戏团像是一个人生的隐喻，使我们得以回想自己是...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30419085/?icn=index-latestbook-subject" title="诗歌十八讲">
                <img src="https://img1.doubanio.com/view/subject/m/public/s30010609.jpg" class=""
                  width="115px" height="172px" alt="诗歌十八讲">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30419085/?icn=index-latestbook-subject"
                  title="诗歌十八讲">诗歌十八讲</a>
              </div>
              <div class="author">
                陈黎&nbsp;/&nbsp;张芬龄
              </div>
              <div class="more-meta">
                <h4 class="title">
                  诗歌十八讲
                </h4>
                <p>
                  <span class="author">
                    陈黎&nbsp;/&nbsp;张芬龄
                  </span>
                  /
                  <span class="year">
                    2019-1-10
                  </span>
                  /
                  <span class="publisher">
                    东方出版社
                  </span>
                </p>
                <p class="abstract"></p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30344071/?icn=index-latestbook-subject" title="雨狗空间">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29971611.jpg" class=""
                  width="115px" height="172px" alt="雨狗空间">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30344071/?icn=index-latestbook-subject"
                  title="雨狗空间">雨狗空间</a>
              </div>
              <div class="author">
                卧斧
              </div>
              <div class="more-meta">
                <h4 class="title">
                  雨狗空间
                </h4>
                <p>
                  <span class="author">
                    卧斧
                  </span>
                  /
                  <span class="year">
                    2019-2
                  </span>
                  /
                  <span class="publisher">
                    后浪丨四川人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  恐怖、战栗、直击心魄
82个可能发生在你我身边的科幻惊悚超短篇故事
平凡无奇的现代社会，在卧斧笔下散发出浓厚的赛博朋克式荒谬感
◎ 编辑推荐
★ 台湾小说家卧斧的 82 个极短篇恐怖故事《雨狗空间》，不读则已，一读就让人头皮发麻停不下来！
★ 办公室被隔成迷宫、捡拾不小心弄掉的头 颅、取下自己的肋骨做琴……通过充满想象力的荒谬怪诞书写，营造赛博朋克式的小说世界...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30406461/?icn=index-latestbook-subject" title="微精通">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29951649.jpg" class=""
                  width="115px" height="172px" alt="微精通">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30406461/?icn=index-latestbook-subject"
                  title="微精通">微精通</a>
              </div>
              <div class="author">
                [英] 罗伯特·特威格尔
              </div>
              <div class="more-meta">
                <h4 class="title">
                  微精通
                </h4>
                <p>
                  <span class="author">
                    [英] 罗伯特·特威格尔
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    后浪丨江西人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  《纽约时报》《新科学家》力荐
妙趣横生的“实践派”学习秘籍
不用努力10000小时
非天才的你也能轻松点满技能树
从门外汉进阶为专业达人！
◎ 编辑推荐
☆ “微精通”是一种开拓性的技能学习方法，只需要找到感兴趣的事物并系统学习，你就能提高自我的学习能力和创造能力，进而将其延伸到工作学习之中，迅速把握新课题的关键。
☆ 以微精通的角度看世界，似乎一切皆有可能。...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30424482/?icn=index-latestbook-subject" title="2018中国年度科幻小说">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30003466.jpg" class=""
                  width="115px" height="172px" alt="2018中国年度科幻小说">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30424482/?icn=index-latestbook-subject"
                  title="2018中国年度科幻小说">2018中国年度科幻小说</a>
              </div>
              <div class="author">
                星河&nbsp;/&nbsp;王逢振
              </div>
              <div class="more-meta">
                <h4 class="title">
                  2018中国年度科幻小说
                </h4>
                <p>
                  <span class="author">
                    星河&nbsp;/&nbsp;王逢振
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    漓江出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  由科幻小说界专业选家选编的2018年度科幻小说，悉数从全国多种相关刊物上精心挑选而来，旨在检阅该年度科幻小说的创作实绩，公正客观地推选出思想性、艺术性俱佳，有代表性、有影响力的年度科幻小说。
陈楸帆《美丽新世界的孤儿》描绘所谓“蛮荒”与“文明”的激烈冲突，探讨稳定社会应该具有的形态；阿缺《宋秀云》以冷静的笔触展现科技状态与现实生活的无缝对接，...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30334629/?icn=index-latestbook-subject" title="星球大战如何征服全宇宙">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30005223.jpg" class=""
                  width="115px" height="172px" alt="星球大战如何征服全宇宙">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30334629/?icn=index-latestbook-subject"
                  title="星球大战如何征服全宇宙">星球大战如何征服全宇宙</a>
              </div>
              <div class="author">
                [美] 克里斯·泰勒
              </div>
              <div class="more-meta">
                <h4 class="title">
                  星球大战如何征服全宇宙
                </h4>
                <p>
                  <span class="author">
                    [美] 克里斯·泰勒
                  </span>
                  /
                  <span class="year">
                    2019-3
                  </span>
                  /
                  <span class="publisher">
                    后浪丨北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  超级IP《星球大战》的全球影响力成长史！
乔治·卢卡斯本人都不敢“面对”的一手资料
演员西蒙·佩吉深情认证，《乔布斯传》作者鼎力推荐
一个故事，如何改变世界的面貌与人类的幻想
造就吸金四百亿的文化与商业传奇
◇◆◇
◎ 编辑推荐
《星球大战》“史学家”、前《时代周刊》《财富》《快公司》撰稿人——克里斯·泰勒带着一肚子问号出发，去寻找全美国最后一个“没有看...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30459512/?icn=index-latestbook-subject" title="妻妾成群（精装典藏版）">
                <img src="https://img1.doubanio.com/view/subject/m/public/s30004389.jpg" class=""
                  width="115px" height="172px" alt="妻妾成群（精装典藏版）">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30459512/?icn=index-latestbook-subject"
                  title="妻妾成群（精装典藏版）">妻妾成群（精装典藏版）</a>
              </div>
              <div class="author">
                苏童
              </div>
              <div class="more-meta">
                <h4 class="title">
                  妻妾成群（精装典藏版）
                </h4>
                <p>
                  <span class="author">
                    苏童
                  </span>
                  /
                  <span class="year">
                    2019-2-1
                  </span>
                  /
                  <span class="publisher">
                    浙江人民出版社
                  </span>
                </p>
                <p class="abstract"></p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30414436/?icn=index-latestbook-subject" title="视觉游戏">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29959731.jpg" class=""
                  width="115px" height="172px" alt="视觉游戏">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30414436/?icn=index-latestbook-subject"
                  title="视觉游戏">视觉游戏</a>
              </div>
              <div class="author">
                [美] 莫莉·邦
              </div>
              <div class="more-meta">
                <h4 class="title">
                  视觉游戏
                </h4>
                <p>
                  <span class="author">
                    [美] 莫莉·邦
                  </span>
                  /
                  <span class="year">
                    2019-2
                  </span>
                  /
                  <span class="publisher">
                    后浪丨湖南美术出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  多位凯迪克金奖得主倾力推荐，生动讲解视觉叙事原理；25周年全新修订纪念版，提高视觉素养的实用宝典！
◎ 编辑推荐
☆ 畅销欧美25年，全新修订珍藏纪念版。
这是一本可以供任何对图像和设计有兴趣的人阅读的书，可以帮助我们轻松识别图像中的视觉要素，提高视觉素养。
☆ 结合日常生活讲设计，设计原理不再枯燥乏味。
在本书中，你不仅可以在耳熟能详的小红帽的故事里深...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30401373/?icn=index-latestbook-subject" title="海风中失落的血色馈赠">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29946431.jpg" class=""
                  width="115px" height="172px" alt="海风中失落的血色馈赠">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30401373/?icn=index-latestbook-subject"
                  title="海风中失落的血色馈赠">海风中失落的血色馈赠</a>
              </div>
              <div class="author">
                [加拿大] 阿利斯泰尔·麦克劳德
              </div>
              <div class="more-meta">
                <h4 class="title">
                  海风中失落的血色馈赠
                </h4>
                <p>
                  <span class="author">
                    [加拿大] 阿利斯泰尔·麦克劳德
                  </span>
                  /
                  <span class="year">
                    2019-1
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract"></p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30412497/?icn=index-latestbook-subject" title="一个观点，不一定对">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30003481.jpg" class=""
                  width="115px" height="172px" alt="一个观点，不一定对">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30412497/?icn=index-latestbook-subject"
                  title="一个观点，不一定对">一个观点，不一定对</a>
              </div>
              <div class="author">
                黄章晋
              </div>
              <div class="more-meta">
                <h4 class="title">
                  一个观点，不一定对
                </h4>
                <p>
                  <span class="author">
                    黄章晋
                  </span>
                  /
                  <span class="year">
                    2019-1-15
                  </span>
                  /
                  <span class="publisher">
                    中国友谊出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  太阳底下，有无数新鲜事
人人都能读懂的科学与新知
一个个生活案例的严肃科学分析，帮你接近生活的真相
对的观点，一个就够了
锤子科技CEO 罗永浩
《舌尖上的中国》《风味人间》导演 陈晓卿
陌陌科技CEO 唐岩
联袂推荐
一本帮你涨姿势的书
一本帮你学会严谨的社会科学逻辑的书
一本帮你看透生活的书
“求知是自我保全的工程。”
本书试图解释的问题，都来自生活中极易观察到的...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30358315/?icn=index-latestbook-subject" title="吴承恩捉妖记 上">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30005383.jpg" class=""
                  width="115px" height="172px" alt="吴承恩捉妖记 上">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30358315/?icn=index-latestbook-subject"
                  title="吴承恩捉妖记 上">吴承恩捉妖记 上</a>
              </div>
              <div class="author">
                有时右逝
              </div>
              <div class="more-meta">
                <h4 class="title">
                  吴承恩捉妖记 上
                </h4>
                <p>
                  <span class="author">
                    有时右逝
                  </span>
                  /
                  <span class="year">
                    2019-2-28
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  ◆ 超人气畅销书作家 有时右逝 热血力作，文字鬼才 马伯庸、才女编剧 海棠 脑洞监制。华语奇幻青春文学，对传统名著的另类解读，再次演绎说不尽的西游。
◆ 经典名著与超强脑洞的碰撞：大明正德年间，皇帝为何抽出极凶之签？镇邪司红钱流落民间，为何反引得一种妖异作祟？少年吴承恩下山捉妖，又是何原因促使他写下西游的不朽传奇？
◆ 微博点击率超2.4亿次，惊艳无数读者...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30354451/?icn=index-latestbook-subject" title="皮肤的秘密">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30009593.jpg" class=""
                  width="115px" height="172px" alt="皮肤的秘密">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30354451/?icn=index-latestbook-subject"
                  title="皮肤的秘密">皮肤的秘密</a>
              </div>
              <div class="author">
                [德]耶尔•阿德勒 (Yael Adler)&nbsp;/&nbsp;[德]卡提雅•史匹哲 (Katja Spitzer )  绘
              </div>
              <div class="more-meta">
                <h4 class="title">
                  皮肤的秘密
                </h4>
                <p>
                  <span class="author">
                    [德]耶尔•阿德勒 (Yael Adler)&nbsp;/&nbsp;[德]卡提雅•史匹哲 (Katja Spitzer )  绘
                  </span>
                  /
                  <span class="year">
                    2019-2-20
                  </span>
                  /
                  <span class="publisher">
                    东方出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  *关于皮肤的17堂课！解读关于人体最大器官的一切！
*内附插图，双色印刷，俏皮生动
*
*德国《明镜周刊》畅销榜首
*亚马逊五星好评
*25国畅销的科学护肤指南
*
*健康传播专家 范志红老师 诚恳推荐
*中国医科大学附属医院皮肤科医生、知乎护理达人 禹汐 认真审定
*
_________________ ______________________________
*
奇妙有趣的皮肤，是心灵的明镜，
是显现我们内心与潜意识...
                </p>
              </div>
            </div>
          </li>
    </ul>

        </div>
      </div>
    </div>
  </div>


  </body>
'''
"""
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)

results = re.findall(pattern, content)
#print(results)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)
