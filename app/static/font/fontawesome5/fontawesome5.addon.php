<?php
if(!defined('__XE__'))
{
	exit();
}

Context::set('fa_prefix', $addon_info->fa_icon_prefix ? $addon_info->fa_icon_prefix : 'fas');

if ($called_position == 'before_display_content' && Context::getResponseMethod() == 'HTML' && Context::get('module') != 'admin')
{
	$fa_path = './addons/fontawesome5/';
	
	$fa_path .= $addon_info->fa_pro == 'Y' ? 'pro/' : 'free/';

	if ($addon_info->fa_load_type == 'css')
	{
		Context::loadFile(array($fa_path . 'css/all.min.css', '', '', null), true);
	}
	else
	{
		Context::loadFile(array($fa_path . 'js/all.min.js', '', '', null), true);
	}
}
