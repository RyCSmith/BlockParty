function toggleGroup(items){
	for (i in items){
		$(items[i]).toggleClass('hide');
	}
}