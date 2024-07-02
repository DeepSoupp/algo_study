function solution(bridge_length, weight, truck_weights) {
   // 몇초 걸리는지 정답값
        let time_answer = 0;
        // 다리길이만큼 배열 만들고 0으로 채움
        let bridge = new Array(bridge_length).fill(0);
        // 다리위 트럭 무게의 합
        let weight_sum = 0;
        // 남은 트럭이 없을때까지 반복
        while (truck_weights.length) {
          // 한번 반복에 1초 증가
          time_answer++; // 6
          // 다리를 나가면 무게 총합에서 나간 트럭의 무게 뺴줌
          weight_sum -= bridge.shift(); // 6
          // 무게합과 다리에 진입하는 트럭 무게의 합이
          // weight 오버하면 더 못올라가니까 다리에 0푸쉬 0은 트럭 없는거
          if (weight_sum + truck_weights[0] > weight) {
            bridge.push(0);
            // 그게 아니면 더 올라갈수 있으므로 남은 트럭중 shift로 앞에서부터
            // 올라가고 무게 총합에 더해줌
          } else {
            const truck = truck_weights.shift();
            bridge.push(truck);
            weight_sum += truck;
          }
        }
        // 남은 트럭은 없으나 마지막트럭이 다리위에 있으므로 다리길이만큼 시간 더해줌
        time_answer += bridge_length;

        return time_answer;
      }