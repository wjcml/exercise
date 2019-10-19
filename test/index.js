const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();
  await page.goto('https://www.lagou.com');

  await page.waitFor(2000);
  // 城市选择关闭，执行默认城市
  // await page.click("#cboxClose")

  // 城市切换
  await page.click("#changeCityBox > ul > li:nth-child(7) > a");
  await page.waitFor(2000);

  // 职位类型列表
  // const pos_type_list = await page.$$eval(".menu_box dl>dd>a", nodes => nodes.map(n => n.innerText))

  // 点击搜索框拟人输入 java
  const pos_type_name = 'java';
  await page.type('.search_input.ui-autocomplete-input', pos_type_name, {delay: 0});
  // 回车
  await page.keyboard.press('Enter');

  await page.waitFor(2000);
  var num = 0;
  var pagethisnum;
  var pagelastnum;
  // 职位url
  while (true){
    // 是否为第一页
    const pager_is_current = await page.$eval(".pager_is_current", nodes => nodes.innerText);
    if(pager_is_current.trim() == "1"){
      const position_url_first = await page.$$eval("ul>li .position>.p_top>a", nodes => nodes.map(n => n.getAttribute("href")));
      console.log(position_url_first);

      pagethisnum = pager_is_current.trim();
      pagelastnum = "";
      num=num+1;
      console.log(num)
    }
    
    const page_next_able = "pager_next";
    const page_next = await page.$eval(".pager_next ", node => node.className);

    // 做判断，连续两次访问地址是否一样

    if(page_next_able == page_next.trim()){
      page.click(".pager_next ");
      await page.waitFor(30000);

      pagelastnum = pagethisnum;
      pagethisnum = await page.$eval(".pager_is_current", nodes => nodes.innerText.trim());

      const position_url = await page.$$eval("ul>li .position>.p_top>a", nodes => nodes.map(n => n.getAttribute("href")));
      console.log(position_url);
      
      num=num+1;
      console.log(num)
    }else{
      console.log("该职位已爬完")
      break;
    }
    
  }


  // await browser.close();
})();