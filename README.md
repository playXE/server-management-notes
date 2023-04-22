# server-management-notes
Just notes on how I manage my home server, some commands I found useful

## Forward host ports to VM 

Tried to solve this problem for a while, solution was VERY simple. Install iptables and enable it. Then just add the following rules:
```sh
iptables -A PREROUTING -t nat -i wlp2s0 -p tcp --dport 2222 -j DNAT --to-destination <vm-addr>:22
iptables -A FORWARD -p tcp -d <vm-addr> --dport 22 -j ACCEPT
# save rules
sh -c 'iptables-save > /etc/iptables/rules.v4' 
```
`<vm-addr>` is VM address. You can get it by running `ip addr` inside VM.
