<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>大理</title>
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous" />
    <script src="./js/jquery-3.5.1.js"></script>
    <SCRIPT type=text/javascript src="js/like.js"></SCRIPT>
    <style>
        /* 美化二级目录容器 */
        .secondary-titles-wrapper {
            display: flex;
            justify-content: center;
            gap: 20px;
            background-color: #ffffff;
            padding: 0px 20px 12px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* 美化二级目录链接 */
        .secondary-titles-wrapper a {
            text-decoration: none;
            color: #333;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .secondary-titles-wrapper a:hover {
            background-color: #d4e0f1;
            color: #1e3a8a;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }

        /* 三级栏目容器 */
        .three-columns-container {
            position: absolute;
            background-color: #ffffff;
            padding: 16px;
            border-radius: 8px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            width: auto; /* 改为auto，根据内容宽度自适应 */
            max-height: 350px;
            overflow-y: auto;
            z-index: 999;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        /* 三级栏目项样式 */
        .three-columns-container a {
            text-decoration: none;
            color: #333;
            font-size: 14px;
            width: 100px; /* 固定宽度 */
            height: 40px; /* 固定高度 */
            padding: 8px 0; /* 调整内边距，使文字居中 */
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            background-color: #f8f8f8;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease;
            flex: 1 1 100px;
            text-align: center;
        }

        .three-columns-container a:hover {
            background-color: #f0f8ff;
            color: #0056b3;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        }

    </style>

</head>

<body>

<%@include file="header.jsp"%>

<div class="jt">
    <div class="main">

        <div id="secondary-titles-container" class="secondary-titles-wrapper">
            <!-- 这里将展示二级标题 -->
        </div>
        <div id="ajaxNewsList"></div>
    </div>
</div>

<%@include file="footer.jsp"%>
<script type="text/javascript">

    function getSecondaryTitles() {
        $.ajax({
            url: '/GetoneLanmuDataServlet',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                if (response && response.success) {
                    $("#secondary-titles-container").empty();
                    var dataLength = response.data.length;
                    for (var i = 0; i < dataLength; i++) {
                        var secondaryTitle = $('<a href="#" class="secontitlelink">' + response.data[i].column_data + '</a>');
                        $("#secondary-titles-container").append(secondaryTitle);
                    }
                } else {
                    console.error('获取二级标题数据失败，错误信息：', response && response.error? response.error : '未知错误');
                }
            },
            error: function () {
                console.error('请求获取二级标题数据失败，请稍后重试。');
            },
            complete: function () {
                handleSecondaryTitleClick();
            }
        });
    }

    function loadNews() {
        console.log("loadnews");
        $.ajax({
            url: 'NewsListServlet',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                if (response.code === 0) {
                    const newsList = response.data;
                    $('#ajaxNewsList').empty();
                    let currentUl;
                    for (let i = 0; i < newsList.length; i++) {
                        if (i % 3 === 0) {
                            // 每三个新闻创建一个新的ul
                            currentUl = $('<ul class="lb"></ul>');
                            $('#ajaxNewsList').append(currentUl);
                        }
                        let newsItem = $('<li>');
                        let newsId = newsList[i].id;
                        // 将新闻id作为参数添加到newsdetail.jsp的链接中
                        newsItem.append('<a href="newsdetail.jsp?id=' + newsId + '">');
                        newsItem.find('a').append('<em><img src="' + newsList[i].image + '" alt="图片"></em>');
                        newsItem.find('a').append('<h3>' + newsList[i].title + '</h3>');
                        newsItem.find('a').append('<p>' + newsList[i].author + "  " + newsList[i].data + '</p>');
                        let hiddenInput = $('<input type="hidden" name="news_id" class="news_id" id="news_id">');
                        hiddenInput.val(newsId);
                        newsItem.find('a').append(hiddenInput);
                        newsItem.find('a').append('</a>');
                        currentUl.append(newsItem);
                    }
                } else {
                    alert("加载新闻失败：" + response.msg);
                }
            },
            error: function () {
                alert("请求失败，请稍后重试。");
            }
        });
    }

    function generateThreeColumnsContainer(response) {
        var threeColumnsContainer = $('<div class="three-columns-container"></div>');
        var dataLength = response.data.length;
        for (var i = 0; i < dataLength; i++) {
            var threeColumnItem = $('<a href="#" class="three-column-link">' + response.data[i].two_column + '</a>');
            threeColumnsContainer.append(threeColumnItem);
            (function (two_column) {
                threeColumnItem.click(function () {
                    var secondaryTitle = response.one_column;
                    var threeColumnTitle = two_column;
                    console.log(secondaryTitle," ",threeColumnTitle);
                    $.ajax({
                        url: 'UpdateNewsByColumnsServlet',
                        type: 'POST',
                        contentType: 'application/json; charset=UTF-8',
                        data: JSON.stringify({
                            "lanmu_column": secondaryTitle,
                            "two_lanmu_column": threeColumnTitle
                        }),
                        dataType: 'json',
                        success: function (response) {
                            if (response && response.code === 0) {
                                const newsList = response.data;
                                $('#ajaxNewsList').empty();
                                let currentUl;
                                for (let i = 0; i < newsList.length; i++) {
                                    if (i % 3 === 0) {
                                        currentUl = $('<ul class="lb"></ul>');
                                        $('#ajaxNewsList').append(currentUl);
                                    }
                                    let newsItem = $('<li>');
                                    let newsId = newsList[i].id;
                                    newsItem.append('<a href="newsdetail.jsp?id=' + newsId + '">');
                                    newsItem.find('a').append('<em><img src="' + newsList[i].image + '" alt="图片"></em>');
                                    newsItem.find('a').append('<h3>' + newsList[i].title + '</h3>');
                                    newsItem.find('a').append('<p>' + newsList[i].author + "  " + newsList[i].data + '</p>');
                                    let hiddenInput = $('<input type="hidden" name="news_id" class="news_id" id="news_id">');
                                    hiddenInput.val(newsId);
                                    newsItem.find('a').append(hiddenInput);
                                    newsItem.find('a').append('</a>');
                                    currentUl.append(newsItem);
                                }
                            } else {
                                alert("更新新闻失败：" + response.msg);
                            }
                        },
                        error: function () {
                            alert("请求更新新闻失败，请稍后重试。");
                        }
                    });
                });
            })(response.data[i].two_column);
        }
        var containerWidth = Math.min(dataLength * 120, 780); // 根据内容宽度调整容器宽度（最多780px）
        threeColumnsContainer.css('width', containerWidth + 'px');
        return threeColumnsContainer;
    }

    function handleSecondaryTitleClick() {
        $('.secontitlelink').click(function () {
            var selectedOption = $(this).text();
            var self = this;

            var existingThreeColumnsContainer = $(".three-columns-container");
            if (existingThreeColumnsContainer.length === 0) {
                $.ajax({
                    url: '/GetThreeColumnsServlet',
                    type: 'POST',  // Change to POST
                    data: JSON.stringify({ one_column: selectedOption }),  // Send JSON data
                    contentType: 'application/json; charset=UTF-8',  // Specify JSON content type
                    dataType: 'json',
                    success: function (response) {
                        if (response && response.success) {
                            var threeColumnsContainer = generateThreeColumnsContainer(response);
                            var scrollTop = $(window).scrollTop();
                            var scrollLeft = $(window).scrollLeft();
                            var elementPosition = $(self).position();

                            // 计算三级栏目容器的位置
                            var topPosition = elementPosition.top + $(self).outerHeight() + scrollTop;
                            var leftPosition = elementPosition.left + (($(self).outerWidth() - threeColumnsContainer.outerWidth()) / 2) + scrollLeft;

                            // 更新三级栏目容器的位置
                            threeColumnsContainer.css({
                                'position': 'absolute',
                                'top': topPosition + 'px',
                                'left': leftPosition + 'px'
                            });

                            $('body').append(threeColumnsContainer);
                        } else {
                            console.error('获取三级栏目数据失败，错误信息：', response && response.error ? response.error : '未知错误');
                        }
                    },
                    error: function () {
                        console.error('请求获取三级栏目数据失败，请稍后重试。');
                    }
                });
            } else {
                existingThreeColumnsContainer.remove();
            }
        });
    }

    function handleThreeColumnClick() {
        // 给三级标题链接添加点击事件
        $('.three-columns-container').on('click', 'a', function () {
            // 获取当前点击的二级标题文本
            var secondaryTitle = $('.secontitlelink.active').text();
            // 获取当前点击的三级标题文本
            var threeColumnTitle = $(this).text();

            $.ajax({
                url: 'UpdateNewsByColumnsServlet',
                type: 'POST',
                contentType: 'application/json; charset=UTF-8',
                data: JSON.stringify({
                    "lanmu_column": secondaryTitle,
                    "two_lanmu_column": threeColumnTitle
                }),
                dataType: 'json',
                success: function (response) {
                    if (response && response.code === 0) {
                        const newsList = response.data;
                        $('#ajaxNewsList').empty();

                        let currentUl;
                        for (let i = 0; i < newsList.length; i++) {

                            if (i % 3 === 0) {
                                // 每三个新闻创建一个新的ul
                                currentUl = $('<ul class="lb"></ul>');
                                $('#ajaxNewsList').append(currentUl);
                            }

                            let newsItem = $('<li>');
                            let newsId = newsList[i].id;
                            // 将新闻id作为参数添加到newsdetail.jsp的链接中
                            newsItem.append('<a href="newsdetail.jsp?id=' + newsId + '">');
                            newsItem.find('a').append('<em><img src="' + newsList[i].image + '" alt="图片"></em>');
                            newsItem.find('a').append('<h3>' + newsList[i].title + '</h3>');
                            newsItem.find('a').append('<p>' + newsList[i].author + "  " + newsList[i].data + '</p>');
                            let hiddenInput = $('<input type="hidden" name="news_id" class="news_id" id="news_id">');
                            hiddenInput.val(newsId);
                            newsItem.find('a').append(hiddenInput);
                            newsItem.find('a').append('</a>');

                            currentUl.append(newsItem);
                        }
                    } else {
                        alert("更新新闻失败：" + response.msg);
                    }
                },
                error: function () {
                    alert("请求更新新闻失败，请稍后重试。");
                }
            });
        });
    }
    $(document).ready(function() {
        $.ajax({
            url: "/getData",
            type: "GET",
            dataType: "json",
            success: function (data) {
                // 检查data中是否有site_description字段
                if (data.site_description) {
                    // 将获取到的简介内容添加到大理简介部分的<p>标签中
                    $('.dl p').html(data.site_description);
                    $('.foot p').first().html(data.title);
                    $('.foot p').eq(1).html(data.keywords);
                    $('.foot a').html(data.email_address);
                    $('.logo img').attr('src', data.logo_image_path);
                }
            },
            error: function () {
                console.error("获取大理简介数据失败");
            }
        });
        getSecondaryTitles();
        loadNews();
        handleThreeColumnClick();
    });

</script>
</body>
</html>