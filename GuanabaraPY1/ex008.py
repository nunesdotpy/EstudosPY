metros = int(input('Uma distância em metros: '))
mm = metros * 1000
cm = metros * 100
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000

print('A medida de {}m corresponde a: '.format(metros))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(km,hm,dam,dm,cm,mm))
