<aside class="nav-sidebar">
        <div class="nav-header"><a href="#"><img src="images/logo.png" alt="logo"></a>
        
        <button class="nav-close"><i
                    class="icofont-close"></i></button></div>
        <div class="nav-content">
            <ul class="nav-list">
                <li><a class="nav-link" href="index.php">Home</a></li>
                <li><a class="nav-link" href="about.php">About Us</a></li>
                <li><a class="nav-link" href="shop.php">Shop</a></li>
                <li><a class="nav-link" href="contact.php">Contact Us</a></li>
                <?php if (isset($_SESSION['customer_id'])) { ?>
                <li><a class="nav-link dropdown-link" href="#">Seller</a>
                                <ul class="dropdown-list">
                                <li><a href="customeraccount.php">Dashboard</a></li>
                                    <li><a href="selectcategory.php">Add Products</a></li>
                                    <li><a href="viewproduct.php">Manage Products</a></li>
                                </ul>
                            </li>
                            <li>
                                <a class="nav-link dropdown-link" href="#">Settings</a>
                                <ul class="dropdown-list">
                                    <li><a href="logout.php">logout</a></li>
                                    <li><a href="change-password.php">change password</a></li>
                                </ul>
                            </li>
                            <?php } elseif (
                                isset($_SESSION['employee_id'])
                            ) { ?>
                            <li><a class="nav-link dropdown-link" href="#"><i class="icofont-lock"></i>Administrator</a>
                                <ul class="dropdown-list">
                                    <li><a href="employeeaccount.php">Dashboard</a></li>
                                    <li><a href="category.php">Add Categories</a></li>
                                    <li><a href="viewcategory.php">Manage Categories</a></li>
                                    <li><a href="viewproduct.php">Manage Products</a></li>
                                    <li><a href="winners.php">View Winners</a></li>
                                </ul>
                            </li>
                            <li>
                                <a class="nav-link dropdown-link" href="#">Settings</a>
                                <ul class="dropdown-list">
                                    <li><a href="logout.php">logout</a></li>
                                    <li><a href="change-password.php">change password</a></li>
                                </ul>
                            </li>
                            <?php } else { ?>
                                <li><a class="nav-link"  href="register.php">Register</a></li>
                                <li><a class="nav-link"  href="login.php">Login</a></li>
                            <?php } ?>
            </ul>
            <!--<div class="nav-info-group">-->
            <!--    <div class="nav-info d-flex justify-content-center">-->
                    
            <!--    </div>-->
            <!--</div>-->
        </div>
    </aside>
    
        <script type="text/javascript"> 
		function display_ct5() {
		var x = new Date()
		var ampm = x.getHours( ) >= 12 ? ' PM' : ' AM';

		var x1=x.getMonth() + 1+ "/" + x.getDate() + "/" + x.getFullYear(); 
		x1 = x.getHours( )+ ":" +  x.getMinutes() + ":" +  x.getSeconds() + ":" + ampm;
		document.getElementById('ct5').innerHTML = x1;
		display_c5();
		}
		function display_c5(){
		var refresh=1000; // Refresh rate in milli seconds
		mytime=setTimeout('display_ct5()',refresh)
		}
		display_c5()
	</script>