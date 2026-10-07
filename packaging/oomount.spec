Name:           oomount
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-bounded filesystem mounter supporting bind mounts and namespaces.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomount
Source0:        oomount-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomount is a sovereign, capability-bounded MOUNT MANAGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomount
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomount-uninstall

%files
/usr/bin/oomount
/usr/bin/oomount-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
