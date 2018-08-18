from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),  # 首页
    url(r'^articles', views.article_list, name='article_list'),  # 文章列表页（支持分页、按分类、按标签）
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_detail, name='article_detail'),  # 文章详情
    url(r'^categories', views.category_list, name='category_list'),  # 所有分类页
    url(r'^tags', views.tag_list, name='tag_list'),  # 所有标签
    url(r'^about', views.about_page, name='about_page'),  # 关于 页面
    url(r'^submit_comment', views.submit_comment, name='submit_comment'),  # 提交评论

    url(r'^editor/article', views.admin_edit_article, name='admin_edit_article'),  # 管理后台编写文章
    url(r'^editor/save', views.admin_edit_save, name='admin_edit_save'),  # 异步保存文章
    url(r'^editor/image_upload', views.admin_image_upload, name='admin_image_upload'),  # 上传图片
]
