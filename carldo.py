<!DOCTYPE html>
<html>
<head>
	<title>Biblioteca virtual UTPN</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<style>
		.book-container {
		  display: flex;
		}
	
		.book-container img {
		  width: 18%;
		  margin-right: 10px;
		}
	
		.window {
		  width: 100px;
		  height: 300px;
		  border: 1px solid black;
		  margin: 10px;
		  text-align: center;
		  display: flex;
		  align-items: center;
		  justify-content: center;
		  font-size: 20px;
		  font-weight: bold;
		}
	  </style>
</head>
<body>
	<header>
		<h1>Biblioteca virtual UTPN</h1></a>
		<img src="img/UTPN.png" alt="Portada" border="2" width="50" height="50" align="TOP">
		<form>
			<input type="text" id="search" name="search" placeholder="Buscar...">
			<button type="submit">Buscar</button>
		</form>

	</header>
	<nav>
		<ul>
			<li><a href="index.html">Inicio</a></li>
			<li><a href="english.html">English</a></li>
			<li><a href="redes.html">Ing. Ciberseguridad</a></li>
			<li><a href="meca.html">Ing. Mecatronica</a></li>
			<li><a href="industrial.html">Ing. Industrial</a></li>
			<li><a href="log.html">Ing. Logistica Internacional</a></li>
			<li><a href="negocio.html">Lic. Gestion de Negocios</a></li>
		</ul>
	</nav>
	<main>
		<h2><span class="highlight">Libros populares</span></h2>
		<ul>
			<li>
				<a href="https://www.u-cursos.cl/ingenieria/2011/2/CC3501/1/material_docente/bajar?id_material=381752">
					<img src="img/python.jpg" border="2" width="100" height="150">>	
					<h5><span class="highlight">Introducción a la programación con Python</span></h5>
				</a>
			</li>
			<li>
				<a href="https://irp.cdn-website.com/7b1aec33/files/uploaded/Libro%20Redes%20de%20Computadoras%2C%205ta%20Edici%C3%B3n%20-%20James%20F.%20Kurose%20_%20Keith%20W.%20Ross%282%29.pdf">
					<img src="img/redes.jpg" border="2" width="100" height="150">>
					<h5><span class="highlight">Redes de computadoras: Un enfoque descendente</span></h5>
				</a>
			</li>
			<li>
				<a href="http://profesores.fi-b.unam.mx/carlos/acs/Libros/Andrew%20Tanenbaum%20-%20Sistemas%20Operativos%20Modernos.pdf">
					<img src="img/SO.jpg"  border="2" width="100" height="150">
					<h5><span class="highlight">Sistemas operativos modernos</span></h5>
				</a>
			</li>
			<li>
				<a href="http://biblioteca.univalle.edu.ni/files/original/d7d963cc9e711380b1b3000027efe4d92f067f32.pdf">
					<img src="img/bd.jpg"  border="2" width="100" height="150">
					<h5><span class="highlight">Bases de datos</span></h5>
				</a>
		</ul>
	</main>
	<footer>
		<p><span class="highlight">&copy; 2023 Biblioteca virtual UTPN</span></p>
	</footer>
</body>
</html>
