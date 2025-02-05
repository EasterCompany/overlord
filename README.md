<h6 align="center" style="border-bottom:0px;padding:9px 0 0 0;"> [ v1.2.20 05/02/2025 ] </h6>
<h1 align="center" style="margin-bottom:32px;border-bottom:0px;"> Overlord </h1>

### Bio

The Overlord Framework, developed by Easter Company, is a lazy full stack framework for developing
Python/Typescript based Web & Mobile applications.

It establishes a development, staging, or production envrionment on a unix system (mac, linux, wsl)
which includes and requires: Nginx, Redis, SQLite, Python 3.12+, Django & Bun.

Wrapping these technologies and filling in the gaps with an integrated CLI for environment based
administration, ops & development.

It's literally "copy and paste this one command and, boom, there's my entire optimisied and minified SaSS infrastructure setup... nice."
don't worry about that stuff. Just develop and deploy to any platform using Python for backend servers and JavaScript or Typescript for
web, ios, andriod, TV, windows, mac, linux client side applications.

[Watch a short introduction video here.](https://www.easter.company/overlord/introduction)

### Install

You can either download the contents of this repository and start building your project that way, or you can install
Overlord's `create-app` command. Which will allow you to create an Overlord App from your terminal. To do so, just copy
the code below into your terminal and hit enter.

```bash
sudo rm /bin/create-app &>/dev/null
sudo wget -P /bin/ https://raw.githubusercontent.com/EasterCompany/RDFS/Prd/Overlord/create-app
sudo chmod +x /bin/create-app
```

### Install Without Sudo

If you don't have sudo permissions or you don't want to install the `create-app` command globally on your system you can
use this as an alternative.

```bash
rm ~/create-app &>/dev/null
wget -P ~/ https://raw.githubusercontent.com/EasterCompany/RDFS/Prd/Overlord/create-app
mv ~/create-app ~/.create-app
chmod +x ~/.create-app
echo 'alias create-app="~/.create-app"' >> ~/.bashrc
```

### Documentation

If you're looking for our beautifully crafted and detailed documentation then you should
[visit our website](https://www.easter.company/overlord).

The documentation also includes a full series of tutorial style videos to guide you in a more entertaining fashion;
however, if you are a well-seasoned professional you may prefer to just read the written format on each page.

### Support

If you're interested in contributing then please get in-touch via this email
[contact@easter.company](mailto:contact@easter.company)
