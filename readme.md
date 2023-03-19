# OmniGraph

Omniverseで使用できるOmniGraphを学習するためのサンプルを貯めていく予定です。     
Omniverse Create 2022.3.3で確認。     

## OmniGraphとは？

Omniverse上での開発をノードの組み合わせで行います。       
OmniGraphはノードを組み合わせて制御（プログラム）を行うためのフレームワークです。     

参考 : https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/Overview.html

![OmniGraph_01.jpg](./images/OmniGraph_01.jpg)     

"Action Graph"を使用することで、あらかじめ用意されたノードを組み合わせることにより、ある程度の動きをOmniverse上で与えることができます。    
アニメーションやPhysicsの制御もOmniGraphで行うことができます。    

また、新しいノードをPythonでExtensionとして記載し、カスタマイズしていくことも可能です。     
また、Python上でWARPを使うことでGPUを使った並列処理を行うことができます。     

* [OmniGraphとAction Graphの違いは ?](./doc/OmniGraph_ActionGraph.md)
* [ノードの構成](./doc/NodeStructure.md)
* [Pythonでカスタムノードを作成](./doc/CustomNode_python.md)

## Extension(Python)を使ったノード作成のサンプル

|Extension名|内容|   
|---|---|   
|[ft_lab.OmniGraph.simpleNode](extensions/ft_lab.OmniGraph.simpleNode)|2つのfloat値を加算して、float値を返す|   


----
