import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RioGrandeDoNorteComponent } from './rio-grande-do-norte.component';

describe('RioGrandeDoNorteComponent', () => {
  let component: RioGrandeDoNorteComponent;
  let fixture: ComponentFixture<RioGrandeDoNorteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RioGrandeDoNorteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RioGrandeDoNorteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
