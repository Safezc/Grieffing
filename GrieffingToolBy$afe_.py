#Coding: UTF-8
#!/usr/local/bin/python3
import socket, time, sys, os, colorama, dns, dns.resolver, subprocess, colorama, requests, base64, os, threading
from colorama import Fore, Style
from colorama import Fore, Back, Style
import queue
from queue import *
import argparse
import time
from random import choice, randrange
import random

##Declaraciones de Funciones ##
def clear():
	clear = os.system("cls || clear")

##BANNER
def banner():

	print(f"""{Fore.LIGHTRED_EX}

░███████╗░█████╗░███████╗███████╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔██╔══╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
╚██████╗░███████║█████╗░░█████╗░░░░░██║░░░██║░░██║██║░░██║██║░░░░░
░╚═██╔██╗██╔══██║██╔══╝░░██╔══╝░░░░░██║░░░██║░░██║██║░░██║██║░░░░░
███████╔╝██║░░██║██║░░░░░███████╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚══════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝


	""")


##MENU##
def menu():
	clear()
	banner()
	print(f"""
{Fore.LIGHTRED_EX}1 - {Fore.LIGHTCYAN_EX}Escanear Puertos
{Fore.LIGHTRED_EX}2 - {Fore.LIGHTCYAN_EX}Escanear Subdominios
{Fore.LIGHTRED_EX}3 - {Fore.LIGHTCYAN_EX}Sacar Dedicados
	\n
	""")

while True:
	banner()
	menu()
	menu_opciones=input(f"{Fore.LIGHTRED_EX}[1/3] > {Fore.WHITE}")
	##Port Scan
	if menu_opciones == "1":
		clear()
		banner()
		print_lock = threading.Lock()
		target = input(f"{Fore.LIGHTRED_EX}IP del servidor > {Fore.WHITE}")
		port1 = input(f"{Fore.LIGHTRED_EX}Epezar Puerto > {Fore.WHITE}")
		port2 = input(f"{Fore.LIGHTRED_EX}Terminar Puerto > {Fore.WHITE}")
		startport = int(port1)
		endport= int(port2)
		print("\n")
		clear()
		banner()
		def portscan(port):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				con = s.connect((target,port))
				with print_lock:
					print(f"{Fore.LIGHTRED_EX}Encontrado > {Fore.WHITE}{target}:{port}")
				con.close()
			except:
				pass

		def threader():
			while  True:
				worker = q.get()
				portscan(worker)
				q.task_done()

		q = Queue()

		for x in range(500):
			t = threading.Thread(target=threader)
			t.daemon = True
			t.start()

		for worker in range(startport,endport):
			q.put(worker)

		q.join()
		print("\n")
		input(f'{Fore.LIGHTRED_EX}> Presiona Enter Para Volver!')

    ##SUBDOMINIOS
	elif menu_opciones == "2":
		clear()
		banner()
		subdomains0 = ["all", "net", "bypass", "rcon", "node010", "node09", "node08", "node07", "node06", "node05", "node04", "node03", "node02", "node01", "supreme", "subnormal", "fun", "aaa", "aa", "a", "kiwi", "server10", "server09", "server08", "server07", "server06", "server05", "server04", "server03", "server02", "server01", "dev", "recuperar", "dedis", "dedicado", "vote", "events", "www", "ovh-birdmc", "cpanel", "ns-vps", "d", "t", "short", "jar", "iptables", "ufw", "recuperar", "baneados", "imagenes", "samp", "social", "holo", "donaciones", "shoprp", "wow", "multicraft", "mail", "radio3", "radio2", "fr", "teamdub", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "docker", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "web", "dev", "tv", "deposito", "depositos", "extra", "extras", "bungee1", "torneoyt", "hcf", "uhc5", "uhc4", "uhc3", "uhc2", "uhc1", "uhc", "dedicado5", "dedicado4", "dedicado3", "dedicado2", "ded5", "ded4", "ded3", "ded2", "ded1", "ded", "gamehitodrh", "servidor4", "webmail", "monitor", "servidor001", "servidor10", "servidor9", "servidor8", "servidor7", "servidor6", "servidor5", "servidor4", "servidor3", "hvokfcic7sm", "autodiscover", "tauchet", "hg10", "ping", "hg9", "hg8", "hg7", "hg6", "hg5", "hg4", "hg3", "hg2", "hg1", "tienda", "status", "ayuda", "playstation", "home", "job", "firewall", "rank", "mantenimiento", "beta", "pay", "private", "port", "bb", "stor", "mx5", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "translations", "staff", "help", "render", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "sv3", "sv2", "sv1",  "vps", "build", "web", "dev", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
		xy = input(f"{Fore.LIGHTRED_EX}Domain > {Fore.WHITE}")
		xyy = xy.lower()
		clear()
		banner()
		print("\n")
		for ejecutar0 in subdomains0:
			try:
				ipserver0 = str(ejecutar0)+"."+str(xyy)
				iphost0 = socket.gethostbyname(str(ipserver0))
				if iphost0.startswith("104."):
					print(f"{Fore.LIGHTRED_EX}Encontrado > {Fore.LIGHTGREEN_EX}{str(ejecutar0)}.{str(xyy)} {Fore.LIGHTCYAN_EX}({str(iphost0)}) {Fore.LIGHTRED_EX}(CloudFlare)")
				else:
					print(f"{Fore.LIGHTRED_EX}Encontrado > {Fore.LIGHTGREEN_EX}{str(ejecutar0)}.{str(xyy)} {Fore.LIGHTCYAN_EX}{str(iphost0)}")
			except:
				pass

		print("\n")
		input(f'{Fore.LIGHTRED_EX}> Presiona Enter Para Volver!')

    ##DEDICADOS
	elif menu_opciones == "3":
		clear()
		banner()
		x = input(f"{Fore.LIGHTRED_EX}Domain > {Fore.WHITE}")
		clear()
		banner()
		print("\n")
		subdomains = ["www", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "render", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
		for execute in subdomains:
			try:
				iphost = str(execute)+"."+str(x)
				ipvic = socket.gethostbyname(iphost)
				socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socka.connect((str(ipvic), int(25565)))
				print(f"{Fore.LIGHTRED_EX}Encontrado > {Fore.LIGHTGREEN_EX}"+ipvic+":25565")
			except:
				pass
		print("\n")
		input(f'{Fore.LIGHTRED_EX}> Presiona Enter Para Volver!')
